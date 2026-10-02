"""
BovDB B1-Structural
===================

Objetivo
--------
Preservar o detector B0 original de TOP/VALLEY e adicionar uma camada
ESTRUTURAL que remove reversões internas pequenas, evitando que cada
micro-oscilação de 1 minuto se torne uma nova fronteira de tendência.

Exemplo:
    B0:
        VALLEY -> TOP -> VALLEY -> TOP

    Se houver:
        - higher low;
        - higher high;
        - correção pequena em relação à pernada anterior;
        - correção pequena em ATR;

    então:
        B1:
        VALLEY --------------------> TOP

O mesmo é aplicado simetricamente para tendência de baixa.

IMPORTANTE
----------
- B0 não é alterado.
- B1 é um pós-processamento separado.
- Thresholds são baseline provisória e devem ser escolhidos depois em VALIDATION.
- Nenhum parâmetro Fuzzy/Choquet é ajustado aqui.
"""

from __future__ import annotations

import sqlite3
import math
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# ============================================================================
# Configuração B1
# ============================================================================

@dataclass(frozen=True)
class StructuralConfig:
    atr_period: int = 14

    # Correção intermediária / impulso anterior.
    # Ex.: 0.45 => correções menores que 45% da perna anterior podem ser micro.
    max_retracement_ratio: float = 0.45

    # Correção intermediária normalizada por ATR.
    # A correção precisa satisfazer AMBOS os critérios para ser removida.
    max_correction_atr: float = 2.00

    # Continuação estrutural mínima:
    # novo topo deve superar o topo anterior e novo vale deve superar o vale anterior
    # (espelhado na tendência de baixa).
    require_hh_hl_structure: bool = True

    # ------------------------------------------------------------------
    # B2 Structural-Significance
    # ------------------------------------------------------------------
    # Caso 1: pivô muito pequeno em termos absolutos de volatilidade.
    b2_max_prominence_atr: float = 1.00

    # Caso 2: pivô ainda relativamente pequeno em ATR E muito assimétrico
    # em relação às pernas vizinhas.
    b2_secondary_prominence_atr: float = 2.00
    b2_max_relative_swing: float = 0.35

    # ------------------------------------------------------------------
    # B3 Regime — SIDEWAYS independente dos pivôs
    # ------------------------------------------------------------------
    sideways_window_multiplier: float = 2.0
    sideways_er_max: float = 0.35
    sideways_slope_atr_max: float = 1.25
    sideways_entry_confirm_bars: int = 3
    sideways_merge_gap_bars: int = 3
    sideways_min_duration_multiplier: float = 1.0

    # Evita divisões patológicas.
    epsilon: float = 1e-12


DEFAULT_CONFIG = StructuralConfig()


# ============================================================================
# Dados e B0 original
# ============================================================================

def load_win_data(db_path, ticker="WINM26", date="2026-04-30"):
    conn = sqlite3.connect(str(db_path))
    query = """
    SELECT
        p.id_ticker, t.ticker, p.date, p.time,
        p.open, p.close, p.high, p.low,
        p.volume, p.business, p.amount_stock
    FROM price1 p
    JOIN ticker t ON p.id_ticker = t.id_ticker
    WHERE t.ticker = ? AND p.date = ?
    ORDER BY p.time ASC
    """
    df = pd.read_sql_query(query, conn, params=(ticker, date))
    conn.close()

    if df.empty:
        raise ValueError(f"Nenhum dado para {ticker} em {date}")

    df["datetime"] = pd.to_datetime(df["date"].astype(str) + " " + df["time"].astype(str))
    df = df.set_index("datetime").sort_index()

    df = df[
        (df.index.time >= pd.to_datetime("09:00:00").time())
        & (df.index.time <= pd.to_datetime("18:35:00").time())
    ].copy()

    return df


def resample_candles(df, timeframe):
    return (
        df.resample(timeframe)
        .agg(
            {
                "open": "first",
                "close": "last",
                "high": "max",
                "low": "min",
                "volume": "sum",
                "business": "sum",
            }
        )
        .dropna()
    )


def detectar_topos_fundos(df_1min, macro_timeframe="15min"):
    """
    B0 original: detecção por direção dos candles macro,
    refinamento em 1 min pelo CLOSE e alternância estrita.
    """
    df_macro = resample_candles(df_1min, macro_timeframe)
    macro_delta = pd.Timedelta(macro_timeframe)

    candidatos = []
    i = 0

    while i < len(df_macro) - 1:
        candle_atual = df_macro.iloc[i]
        candle_atual_alta = candle_atual["close"] > candle_atual["open"]
        candle_atual_baixa = candle_atual["close"] <= candle_atual["open"]

        if candle_atual_alta:
            sequencia_alta = [candle_atual]

            while (
                i + 1 < len(df_macro)
                and df_macro.iloc[i + 1]["close"] > df_macro.iloc[i + 1]["open"]
            ):
                i += 1
                sequencia_alta.append(df_macro.iloc[i])

            candle_topo = max(sequencia_alta, key=lambda x: x["close"])

            intervalo_micro = df_1min[
                (df_1min.index >= candle_topo.name)
                & (df_1min.index < candle_topo.name + macro_delta)
            ]

            if not intervalo_micro.empty:
                maior_close = intervalo_micro["close"].max()
                candle_micro_topo = intervalo_micro[
                    intervalo_micro["close"] == maior_close
                ].iloc[0]

                candidatos.append(
                    (
                        candle_micro_topo.name,
                        float(candle_micro_topo["close"]),
                        float(candle_micro_topo["high"]),
                        "topo",
                    )
                )

                if i + 1 < len(df_macro):
                    prox_candle = df_macro.iloc[i + 1]

                    prox_intervalo = df_1min[
                        (df_1min.index >= prox_candle.name)
                        & (df_1min.index < prox_candle.name + macro_delta)
                    ]

                    if not prox_intervalo.empty:
                        maior_close_prox = prox_intervalo["close"].max()

                        if maior_close_prox > maior_close:
                            candle_micro_topo_prox = prox_intervalo[
                                prox_intervalo["close"] == maior_close_prox
                            ].iloc[0]

                            candidatos[-1] = (
                                candle_micro_topo_prox.name,
                                float(candle_micro_topo_prox["close"]),
                                float(candle_micro_topo_prox["high"]),
                                "topo",
                            )

        elif candle_atual_baixa:
            sequencia_baixa = [candle_atual]

            while (
                i + 1 < len(df_macro)
                and df_macro.iloc[i + 1]["close"] < df_macro.iloc[i + 1]["open"]
            ):
                i += 1
                sequencia_baixa.append(df_macro.iloc[i])

            candle_fundo = min(sequencia_baixa, key=lambda x: x["close"])

            intervalo_micro = df_1min[
                (df_1min.index >= candle_fundo.name)
                & (df_1min.index < candle_fundo.name + macro_delta)
            ]

            if not intervalo_micro.empty:
                menor_close = intervalo_micro["close"].min()
                candle_micro_fundo = intervalo_micro[
                    intervalo_micro["close"] == menor_close
                ].iloc[0]

                candidatos.append(
                    (
                        candle_micro_fundo.name,
                        float(candle_micro_fundo["close"]),
                        float(candle_micro_fundo["low"]),
                        "vale",
                    )
                )

                if i + 1 < len(df_macro):
                    prox_candle = df_macro.iloc[i + 1]

                    prox_intervalo = df_1min[
                        (df_1min.index >= prox_candle.name)
                        & (df_1min.index < prox_candle.name + macro_delta)
                    ]

                    if not prox_intervalo.empty:
                        menor_close_prox = prox_intervalo["close"].min()

                        if menor_close_prox < menor_close:
                            candle_micro_fundo_prox = prox_intervalo[
                                prox_intervalo["close"] == menor_close_prox
                            ].iloc[0]

                            candidatos[-1] = (
                                candle_micro_fundo_prox.name,
                                float(candle_micro_fundo_prox["close"]),
                                float(candle_micro_fundo_prox["low"]),
                                "vale",
                            )

        i += 1

    candidatos.sort(key=lambda x: x[0])

    if not candidatos:
        return [], [], []

    alternados = [candidatos[0]]

    for c in candidatos[1:]:
        tipo = c[3]
        ultimo = alternados[-1]

        if tipo == ultimo[3]:
            if tipo == "topo":
                if c[2] > ultimo[2]:
                    alternados[-1] = c
            else:
                if c[2] < ultimo[2]:
                    alternados[-1] = c
        else:
            alternados.append(c)

    topos = []
    fundos = []
    pontos_confirmacao = []

    for dt, close, extremo, tipo in alternados:
        if tipo == "topo":
            topos.append((dt, close, extremo))
        else:
            fundos.append((dt, close, extremo))

        pontos_confirmacao.append((dt, extremo))

    return topos, fundos, pontos_confirmacao


# ============================================================================
# Estruturas auxiliares
# ============================================================================

def compute_atr(df, period=14):
    prev_close = df["close"].shift(1)

    tr = pd.concat(
        [
            df["high"] - df["low"],
            (df["high"] - prev_close).abs(),
            (df["low"] - prev_close).abs(),
        ],
        axis=1,
    ).max(axis=1)

    return tr.rolling(
        period,
        min_periods=max(2, period // 3),
    ).mean()


def pivots_from_b0(topos, fundos):
    pivots = []

    for dt, close, extreme in topos:
        pivots.append(
            {
                "time": pd.Timestamp(dt),
                "type": "TOP",
                "close": float(close),
                "price": float(extreme),
            }
        )

    for dt, close, extreme in fundos:
        pivots.append(
            {
                "time": pd.Timestamp(dt),
                "type": "VALLEY",
                "close": float(close),
                "price": float(extreme),
            }
        )

    pivots.sort(key=lambda p: p["time"])
    return pivots


def median_atr_between(atr, start, end, fallback=1.0):
    values = atr.loc[(atr.index >= start) & (atr.index <= end)]
    values = values.replace([np.inf, -np.inf], np.nan).dropna()

    if len(values):
        value = float(values.median())
        if np.isfinite(value) and value > 0:
            return value

    return float(fallback)


# ============================================================================
# B1 Structural Filter
# ============================================================================

def analyze_four_pivots(p0, p1, p2, p3, atr, cfg=DEFAULT_CONFIG):
    """
    Avalia se p1 e p2 são uma correção interna que pode ser removida.

    UP continuation:
        VALLEY p0 -> TOP p1 -> VALLEY p2 -> TOP p3
        com HL + HH

        impulso      = p1 - p0
        correção     = p1 - p2
        retracement  = correção / impulso

    DOWN continuation:
        TOP p0 -> VALLEY p1 -> TOP p2 -> VALLEY p3
        com LH + LL

        impulso      = p0 - p1
        correção     = p2 - p1
        retracement  = correção / impulso
    """
    types = [p["type"] for p in (p0, p1, p2, p3)]

    up_pattern = types == ["VALLEY", "TOP", "VALLEY", "TOP"]
    down_pattern = types == ["TOP", "VALLEY", "TOP", "VALLEY"]

    if not up_pattern and not down_pattern:
        return {
            "remove_middle": False,
            "reason": "pattern_not_continuation",
        }

    atr_ref = median_atr_between(
        atr,
        p1["time"],
        p2["time"],
        fallback=1.0,
    )

    if up_pattern:
        impulse = float(p1["price"] - p0["price"])
        correction = float(p1["price"] - p2["price"])

        higher_low = p2["price"] > p0["price"]
        higher_high = p3["price"] > p1["price"]

        structure_ok = higher_low and higher_high

        structure_name = "HH_HL"

    else:
        impulse = float(p0["price"] - p1["price"])
        correction = float(p2["price"] - p1["price"])

        lower_high = p2["price"] < p0["price"]
        lower_low = p3["price"] < p1["price"]

        structure_ok = lower_high and lower_low

        structure_name = "LH_LL"

    if impulse <= cfg.epsilon or correction < 0:
        return {
            "remove_middle": False,
            "reason": "invalid_geometry",
            "structure": structure_name,
        }

    retracement_ratio = correction / max(impulse, cfg.epsilon)
    correction_atr = correction / max(atr_ref, cfg.epsilon)

    if cfg.require_hh_hl_structure:
        structural_continuation = structure_ok
    else:
        structural_continuation = True

    small_retracement = retracement_ratio <= cfg.max_retracement_ratio
    small_atr_correction = correction_atr <= cfg.max_correction_atr

    remove = (
        structural_continuation
        and small_retracement
        and small_atr_correction
    )

    return {
        "remove_middle": bool(remove),
        "reason": (
            "micro_correction"
            if remove
            else "structural_reversal_or_large_correction"
        ),
        "structure": structure_name,
        "structure_ok": bool(structure_ok),
        "impulse_points": float(impulse),
        "correction_points": float(correction),
        "retracement_ratio": float(retracement_ratio),
        "atr_reference": float(atr_ref),
        "correction_atr": float(correction_atr),
        "small_retracement": bool(small_retracement),
        "small_atr_correction": bool(small_atr_correction),
    }


def structural_filter_pivots(
    df_1min,
    pivots,
    cfg=DEFAULT_CONFIG,
):
    """
    Compressão iterativa de micro-reversões.

    Quando [p0,p1,p2,p3] representa continuação da estrutura,
    p1 e p2 são removidos:

        [VALLEY, TOP, VALLEY, TOP] -> [VALLEY, TOP]

    O processo reinicia e continua até nenhuma remoção ser possível.
    """
    pivots = [dict(p) for p in sorted(pivots, key=lambda x: x["time"])]

    if len(pivots) < 4:
        return pivots, []

    atr = compute_atr(df_1min, cfg.atr_period)
    removals = []

    changed = True
    pass_number = 0

    while changed and len(pivots) >= 4:
        changed = False
        pass_number += 1

        i = 0

        while i <= len(pivots) - 4:
            p0, p1, p2, p3 = pivots[i : i + 4]

            analysis = analyze_four_pivots(
                p0,
                p1,
                p2,
                p3,
                atr,
                cfg=cfg,
            )

            if analysis.get("remove_middle", False):
                removals.append(
                    {
                        "pass": pass_number,
                        "anchor_start_time": p0["time"],
                        "removed_pivot_1_time": p1["time"],
                        "removed_pivot_1_type": p1["type"],
                        "removed_pivot_1_price": p1["price"],
                        "removed_pivot_2_time": p2["time"],
                        "removed_pivot_2_type": p2["type"],
                        "removed_pivot_2_price": p2["price"],
                        "anchor_end_time": p3["time"],
                        **analysis,
                    }
                )

                # Remove pivôs intermediários.
                del pivots[i + 1 : i + 3]

                changed = True

                # Reavaliar contexto anterior após a compressão.
                i = max(i - 2, 0)
                continue

            i += 1

    return pivots, removals



# ============================================================================
# B2 Structural-Significance
# ============================================================================

def analyze_local_significance(prev_pivot, center_pivot, next_pivot, atr, cfg=DEFAULT_CONFIG):
    """
    Avalia um pivô central entre dois pivôs do mesmo tipo.

    Exemplo de continuação de baixa:
        VALLEY_prev -> TOP_center -> VALLEY_next
        com VALLEY_next < VALLEY_prev

    Exemplo de continuação de alta:
        TOP_prev -> VALLEY_center -> TOP_next
        com TOP_next > TOP_prev

    A importância local do pivô central é:

        local_prominence = min(left_leg, right_leg)
        prominence_atr   = local_prominence / ATR
        relative_swing   = min(left_leg, right_leg) / max(left_leg, right_leg)

    O pivô é considerado micro quando a direção estrutural continua e:

        prominence_atr <= b2_max_prominence_atr

    OU

        prominence_atr <= b2_secondary_prominence_atr
        AND relative_swing <= b2_max_relative_swing

    A segunda regra captura pequenos repiques muito assimétricos dentro
    de uma perna estrutural maior.
    """
    if prev_pivot["type"] != next_pivot["type"]:
        return {
            "remove_center": False,
            "reason": "neighbors_not_same_type",
        }

    if center_pivot["type"] == prev_pivot["type"]:
        return {
            "remove_center": False,
            "reason": "sequence_not_alternating",
        }

    if (
        center_pivot["type"] == "TOP"
        and prev_pivot["type"] == "VALLEY"
        and next_pivot["type"] == "VALLEY"
    ):
        structural_direction = "DOWN"
        continuation = next_pivot["price"] < prev_pivot["price"]

    elif (
        center_pivot["type"] == "VALLEY"
        and prev_pivot["type"] == "TOP"
        and next_pivot["type"] == "TOP"
    ):
        structural_direction = "UP"
        continuation = next_pivot["price"] > prev_pivot["price"]

    else:
        return {
            "remove_center": False,
            "reason": "unsupported_pattern",
        }

    left_leg = abs(float(center_pivot["price"]) - float(prev_pivot["price"]))
    right_leg = abs(float(next_pivot["price"]) - float(center_pivot["price"]))

    local_prominence = min(left_leg, right_leg)
    max_leg = max(left_leg, right_leg)

    atr_ref = median_atr_between(
        atr,
        prev_pivot["time"],
        next_pivot["time"],
        fallback=1.0,
    )

    prominence_atr = local_prominence / max(atr_ref, cfg.epsilon)

    relative_swing = (
        local_prominence / max(max_leg, cfg.epsilon)
        if max_leg > cfg.epsilon
        else 0.0
    )

    very_small_absolute = (
        prominence_atr <= cfg.b2_max_prominence_atr
    )

    weak_and_asymmetric = (
        prominence_atr <= cfg.b2_secondary_prominence_atr
        and relative_swing <= cfg.b2_max_relative_swing
    )

    remove = bool(
        continuation
        and (very_small_absolute or weak_and_asymmetric)
    )

    if remove:
        if very_small_absolute:
            reason = "low_prominence_atr"
        else:
            reason = "weak_asymmetric_swing"
    elif not continuation:
        reason = "structural_direction_changed"
    else:
        reason = "pivot_significant"

    return {
        "remove_center": remove,
        "reason": reason,
        "structural_direction": structural_direction,
        "continuation": bool(continuation),
        "left_leg_points": float(left_leg),
        "right_leg_points": float(right_leg),
        "local_prominence_points": float(local_prominence),
        "atr_reference": float(atr_ref),
        "prominence_atr": float(prominence_atr),
        "relative_swing": float(relative_swing),
        "very_small_absolute": bool(very_small_absolute),
        "weak_and_asymmetric": bool(weak_and_asymmetric),
    }


def _choose_structural_same_type(a, b):
    """
    Quando o pivô central é removido, os vizinhos tornam-se consecutivos
    e têm o mesmo tipo. Mantém o extremo estruturalmente dominante:
      TOP    -> maior preço
      VALLEY -> menor preço
    """
    if a["type"] != b["type"]:
        raise ValueError("Expected same-type pivots")

    if a["type"] == "TOP":
        return a if a["price"] >= b["price"] else b

    return a if a["price"] <= b["price"] else b


def structural_significance_filter(
    df_1min,
    pivots,
    cfg=DEFAULT_CONFIG,
):
    """
    B2: simplificação iterativa de baixa significância local.

    Entrada:
        pivôs já filtrados pela B1.

    Processo:
      1. avalia cada tripla [prev, center, next];
      2. exige continuidade estrutural entre prev e next;
      3. mede prominence/ATR e relative_swing do center;
      4. remove o center se for micro;
      5. prev e next ficam do mesmo tipo;
      6. mantém somente o mais extremo dos dois;
      7. reavalia a sequência até convergir.

    Portanto, uma sequência:

        TOP -> VALLEY -> small TOP -> LOWER VALLEY

    pode virar:

        TOP -----------------------> LOWER VALLEY
    """
    pivots = [
        dict(p)
        for p in sorted(pivots, key=lambda x: x["time"])
    ]

    if len(pivots) < 3:
        return pivots, []

    atr = compute_atr(df_1min, cfg.atr_period)

    removals = []
    changed = True
    pass_number = 0

    while changed and len(pivots) >= 3:
        changed = False
        pass_number += 1
        i = 1

        while i <= len(pivots) - 2:
            prev_pivot = pivots[i - 1]
            center_pivot = pivots[i]
            next_pivot = pivots[i + 1]

            analysis = analyze_local_significance(
                prev_pivot,
                center_pivot,
                next_pivot,
                atr,
                cfg=cfg,
            )

            if analysis.get("remove_center", False):
                survivor = _choose_structural_same_type(
                    prev_pivot,
                    next_pivot,
                )

                dominated_neighbor = (
                    next_pivot
                    if survivor is prev_pivot
                    else prev_pivot
                )

                removals.append(
                    {
                        "pass": pass_number,
                        "removed_center_time": center_pivot["time"],
                        "removed_center_type": center_pivot["type"],
                        "removed_center_price": center_pivot["price"],
                        "removed_same_type_neighbor_time": dominated_neighbor["time"],
                        "removed_same_type_neighbor_type": dominated_neighbor["type"],
                        "removed_same_type_neighbor_price": dominated_neighbor["price"],
                        "survivor_time": survivor["time"],
                        "survivor_type": survivor["type"],
                        "survivor_price": survivor["price"],
                        **analysis,
                    }
                )

                # Substitui a tripla pelo pivô estrutural dominante.
                pivots[i - 1 : i + 2] = [dict(survivor)]

                changed = True
                i = max(1, i - 2)
                continue

            i += 1

    return pivots, removals


# ============================================================================
# Trend labels binários gerados por B0 ou B1
# ============================================================================

def pivots_to_binary_trend_labels(df_1min, pivots):
    """
    Convenção:
      primeiro pivô VALLEY => prefixo é DOWNTREND (0)
      primeiro pivô TOP    => prefixo é UPTREND   (1)

      VALLEY -> TOP : (VALLEY, TOP] = UPTREND
      TOP -> VALLEY : (TOP, VALLEY] = DOWNTREND

      após último pivô => unlabeled
    """
    out = pd.DataFrame(index=df_1min.index)
    out["trend_label"] = pd.Series(pd.NA, index=out.index, dtype="Int64")
    out["trend_name"] = None
    out["segment_end_time"] = pd.NaT
    out["segment_end_type"] = None

    if not pivots:
        return out

    first = pivots[0]

    if first["type"] == "VALLEY":
        prefix_label = 0
        prefix_name = "DOWNTREND"
    else:
        prefix_label = 1
        prefix_name = "UPTREND"

    mask = out.index <= first["time"]
    out.loc[mask, "trend_label"] = prefix_label
    out.loc[mask, "trend_name"] = prefix_name
    out.loc[mask, "segment_end_time"] = first["time"]
    out.loc[mask, "segment_end_type"] = first["type"]

    for start, end in zip(pivots[:-1], pivots[1:]):
        mask = (out.index > start["time"]) & (out.index <= end["time"])

        if start["type"] == "VALLEY" and end["type"] == "TOP":
            label = 1
            name = "UPTREND"
        elif start["type"] == "TOP" and end["type"] == "VALLEY":
            label = 0
            name = "DOWNTREND"
        else:
            # Não deveria ocorrer após B0/B1.
            continue

        out.loc[mask, "trend_label"] = label
        out.loc[mask, "trend_name"] = name
        out.loc[mask, "segment_end_time"] = end["time"]
        out.loc[mask, "segment_end_type"] = end["type"]

    return out




# ============================================================================
# B3 Regime — SIDEWAYS independente dos pivôs
# ============================================================================

DOWNTREND_3C = 0
SIDEWAYS_3C = 1
UPTREND_3C = 2


def timeframe_minutes(timeframe):
    return int(pd.Timedelta(timeframe).total_seconds() // 60)


def _odd_window_size(timeframe, cfg=DEFAULT_CONFIG):
    minutes = timeframe_minutes(timeframe)
    w = max(5, int(round(minutes * cfg.sideways_window_multiplier)))
    if w % 2 == 0:
        w += 1
    return w


def _window_efficiency_ratio(closes, epsilon=1e-12):
    arr = np.asarray(closes, dtype=float)
    if arr.size < 2:
        return np.nan
    path = np.abs(np.diff(arr)).sum()
    if not np.isfinite(path) or path <= epsilon:
        return 0.0
    return float(np.clip(abs(arr[-1] - arr[0]) / path, 0.0, 1.0))


def _window_slope_atr(closes, atr_ref, epsilon=1e-12):
    arr = np.asarray(closes, dtype=float)
    if arr.size < 2:
        return np.nan
    x = np.arange(arr.size, dtype=float)
    slope = float(np.polyfit(x, arr, 1)[0])
    return float(
        abs(slope) * max(arr.size - 1, 1) / max(float(atr_ref), epsilon)
    )


def compute_sideways_features(df_1min, timeframe, cfg=DEFAULT_CONFIG):
    """
    Janela CENTRADA, logo ex-post:
      ER baixo + slope/ATR baixo => candidato SIDEWAYS.
    """
    df = df_1min.copy()
    atr = compute_atr(df, cfg.atr_period)

    window = _odd_window_size(timeframe, cfg)
    half = window // 2

    result = pd.DataFrame(index=df.index)
    result["sideways_er"] = np.nan
    result["sideways_slope_atr"] = np.nan
    result["sideways_net_atr"] = np.nan
    result["sideways_range_atr"] = np.nan
    result["sideways_raw"] = False

    for i in range(half, len(df) - half):
        segment = df.iloc[i - half:i + half + 1]
        closes = segment["close"].astype(float).to_numpy()

        atr_values = (
            atr.loc[segment.index]
            .replace([np.inf, -np.inf], np.nan)
            .dropna()
        )
        if len(atr_values):
            atr_ref = float(atr_values.median())
        else:
            ranges = (segment["high"] - segment["low"]).replace(0, np.nan).dropna()
            atr_ref = float(ranges.median()) if len(ranges) else 1.0

        if not np.isfinite(atr_ref) or atr_ref <= cfg.epsilon:
            atr_ref = 1.0

        er = _window_efficiency_ratio(closes, cfg.epsilon)
        slope_atr = _window_slope_atr(closes, atr_ref, cfg.epsilon)
        net_atr = abs(float(closes[-1]) - float(closes[0])) / max(atr_ref, cfg.epsilon)
        range_atr = float(segment["high"].max() - segment["low"].min()) / max(atr_ref, cfg.epsilon)

        ts = df.index[i]
        result.loc[ts, "sideways_er"] = er
        result.loc[ts, "sideways_slope_atr"] = slope_atr
        result.loc[ts, "sideways_net_atr"] = net_atr
        result.loc[ts, "sideways_range_atr"] = range_atr
        result.loc[ts, "sideways_raw"] = bool(
            er <= cfg.sideways_er_max
            and slope_atr <= cfg.sideways_slope_atr_max
        )

    return result


def _true_runs(mask):
    arr = np.asarray(mask, dtype=bool)
    runs = []
    start = None

    for i, value in enumerate(arr):
        if value and start is None:
            start = i

        if start is not None and (not value or i == len(arr) - 1):
            end = i if value and i == len(arr) - 1 else i - 1
            runs.append((start, end))
            start = None

    return runs


def detect_sideways_regions(df_1min, timeframe, cfg=DEFAULT_CONFIG, b2_pivots=None):
    """
    SIDEWAYS tem início e fim próprios, não depende de pivô A -> pivô B.
    """
    features = compute_sideways_features(df_1min, timeframe, cfg=cfg)
    raw = features["sideways_raw"].fillna(False).to_numpy(dtype=bool)

    runs = [
        r for r in _true_runs(raw)
        if (r[1] - r[0] + 1) >= cfg.sideways_entry_confirm_bars
    ]

    # Merge de pequenos gaps.
    merged = []
    for run in runs:
        if not merged:
            merged.append(list(run))
            continue

        gap = run[0] - merged[-1][1] - 1
        if gap <= cfg.sideways_merge_gap_bars:
            merged[-1][1] = run[1]
        else:
            merged.append(list(run))

    tf_minutes = timeframe_minutes(timeframe)
    min_duration = max(
        cfg.sideways_entry_confirm_bars,
        int(math.ceil(tf_minutes * cfg.sideways_min_duration_multiplier)),
    )

    pivots = b2_pivots or []
    regions = []

    for start_i, end_i in merged:
        n_bars = end_i - start_i + 1
        if n_bars < min_duration:
            continue

        start = features.index[start_i]
        end = features.index[end_i]

        local = features.iloc[start_i:end_i + 1]
        price_segment = df_1min.loc[start:end]
        internal_pivots = [
            p for p in pivots
            if start <= p["time"] <= end
        ]

        regions.append({
            "start": pd.Timestamp(start),
            "end": pd.Timestamp(end),
            "duration_minutes": float((end - start).total_seconds() / 60.0 + 1.0),
            "n_bars": int(n_bars),
            "mean_er": float(local["sideways_er"].mean()),
            "max_er": float(local["sideways_er"].max()),
            "mean_slope_atr": float(local["sideways_slope_atr"].mean()),
            "max_slope_atr": float(local["sideways_slope_atr"].max()),
            "mean_net_atr": float(local["sideways_net_atr"].mean()),
            "range_points": float(price_segment["high"].max() - price_segment["low"].min()),
            "internal_b2_pivots": int(len(internal_pivots)),
        })

    return features, regions


def timestamp_in_sideways(ts, regions):
    ts = pd.Timestamp(ts)
    return any(r["start"] <= ts <= r["end"] for r in regions)


def _enforce_alternation_after_sideways(pivots):
    ordered = sorted([dict(p) for p in pivots], key=lambda p: p["time"])

    if not ordered:
        return [], []

    kept = [ordered[0]]
    dominated = []

    for p in ordered[1:]:
        last = kept[-1]

        if p["type"] != last["type"]:
            kept.append(p)
            continue

        if p["type"] == "TOP":
            survivor = p if p["price"] > last["price"] else last
        else:
            survivor = p if p["price"] < last["price"] else last

        removed = last if survivor is p else p

        dominated.append({
            "time": removed["time"],
            "type": removed["type"],
            "price": removed["price"],
            "reason": "same_type_after_sideways_suppression",
        })

        kept[-1] = survivor

    return kept, dominated


def suppress_pivots_inside_sideways(b2_pivots, regions):
    """
    Regra central:
      dentro de SIDEWAYS não existe TOP/VALLEY estrutural.
    """
    kept = []
    suppressed = []

    for p in b2_pivots:
        region = next(
            (r for r in regions if r["start"] <= p["time"] <= r["end"]),
            None,
        )

        if region is None:
            kept.append(dict(p))
        else:
            suppressed.append({
                "time": p["time"],
                "type": p["type"],
                "price": p["price"],
                "sideways_start": region["start"],
                "sideways_end": region["end"],
                "reason": "inside_sideways",
            })

    kept, dominated = _enforce_alternation_after_sideways(kept)
    return kept, suppressed, dominated


def build_three_class_regime_labels(
    df_1min,
    b2_binary_labels,
    sideways_features,
    sideways_regions,
):
    """
    0 = DOWNTREND
    1 = SIDEWAYS
    2 = UPTREND
    """
    out = df_1min[["open", "high", "low", "close"]].copy()

    if "volume" in df_1min.columns:
        out["volume"] = df_1min["volume"]

    out["b2_binary_label"] = b2_binary_labels["trend_label"]

    out["trend_label"] = pd.Series(pd.NA, index=out.index, dtype="Int64")
    out["trend_name"] = None

    down_mask = out["b2_binary_label"] == 0
    up_mask = out["b2_binary_label"] == 1

    out.loc[down_mask, "trend_label"] = DOWNTREND_3C
    out.loc[down_mask, "trend_name"] = "DOWNTREND"

    out.loc[up_mask, "trend_label"] = UPTREND_3C
    out.loc[up_mask, "trend_name"] = "UPTREND"

    for col in [
        "sideways_er",
        "sideways_slope_atr",
        "sideways_net_atr",
        "sideways_range_atr",
        "sideways_raw",
    ]:
        out[col] = sideways_features[col]

    out["sideways_region"] = False
    out["sideways_region_id"] = pd.Series(pd.NA, index=out.index, dtype="Int64")

    for region_id, r in enumerate(sideways_regions, start=1):
        mask = (out.index >= r["start"]) & (out.index <= r["end"])

        out.loc[mask, "trend_label"] = SIDEWAYS_3C
        out.loc[mask, "trend_name"] = "SIDEWAYS"
        out.loc[mask, "sideways_region"] = True
        out.loc[mask, "sideways_region_id"] = region_id

    return out


def _line_with_sideways_gaps(pivots, regions):
    if not pivots:
        return [], []

    x = [pivots[0]["time"]]
    y = [pivots[0]["price"]]

    for i in range(1, len(pivots)):
        prev = pivots[i - 1]
        curr = pivots[i]

        crosses = any(
            not (r["end"] < prev["time"] or r["start"] > curr["time"])
            for r in regions
        )

        if crosses:
            x.extend([None, curr["time"]])
            y.extend([None, curr["price"]])
        else:
            x.append(curr["time"])
            y.append(curr["price"])

    return x, y


# ============================================================================
# Summary
# ============================================================================

def structural_summary(
    b0_pivots,
    b1_pivots,
    b2_pivots,
    b3_pivots,
    sideways_regions,
    b3_labels,
    df_1min,
):
    session_minutes = max(
        (df_1min.index[-1] - df_1min.index[0]).total_seconds() / 60.0,
        1.0,
    )
    hours = session_minutes / 60.0

    labeled = b3_labels["trend_label"].dropna()
    counts = labeled.value_counts().to_dict() if len(labeled) else {}

    sideways_minutes = sum(r["duration_minutes"] for r in sideways_regions)

    return {
        "b0_pivots": len(b0_pivots),
        "b1_pivots": len(b1_pivots),
        "b2_pivots": len(b2_pivots),
        "b3_pivots": len(b3_pivots),
        "removed_b3": len(b2_pivots) - len(b3_pivots),
        "sideways_regions": len(sideways_regions),
        "sideways_minutes": float(sideways_minutes),
        "sideways_session_fraction": float(sideways_minutes / session_minutes),
        "down_candles": int(counts.get(DOWNTREND_3C, 0)),
        "sideways_candles": int(counts.get(SIDEWAYS_3C, 0)),
        "up_candles": int(counts.get(UPTREND_3C, 0)),
        "b3_pivots_per_hour": len(b3_pivots) / hours,
        "b3_pivot_compression_vs_b0": (
            len(b3_pivots) / len(b0_pivots) if len(b0_pivots) else np.nan
        ),
    }


# ============================================================================
# Dashboard B3
# ============================================================================

def _duration_ms(start, end):
    return max((end - start).total_seconds() * 1000.0, 60_000.0)


def _midpoint(start, end):
    return start + (end - start) / 2


def build_comparison_dashboard(df_1min, per_timeframe, ticker, date, cfg=DEFAULT_CONFIG):
    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.03,
        row_heights=[0.83, 0.17],
    )

    COLOR_CANDLE_UP = "#00C853"
    COLOR_CANDLE_DOWN = "#FF1744"
    COLOR_TOP = "#00E676"
    COLOR_BOTTOM = "#FF1744"

    line_colors = {
        "15min": "#00E5FF",
        "10min": "#FFB300",
        "5min": "#D500F9",
    }

    COLOR_B2 = "rgba(190,190,190,0.40)"
    COLOR_SIDEWAYS = "rgba(255, 179, 0, 0.18)"
    COLOR_SUPPRESSED = "#FFB300"

    fig.add_trace(
        go.Candlestick(
            x=df_1min.index,
            open=df_1min["open"],
            high=df_1min["high"],
            low=df_1min["low"],
            close=df_1min["close"],
            name="Candles 1 min",
            increasing_line_color=COLOR_CANDLE_UP,
            decreasing_line_color=COLOR_CANDLE_DOWN,
            increasing_fillcolor=COLOR_CANDLE_UP,
            decreasing_fillcolor=COLOR_CANDLE_DOWN,
            increasing_line_width=1.2,
            decreasing_line_width=1.2,
            hoverinfo="all",
        ),
        row=1,
        col=1,
    )

    has_vol = "volume" in df_1min.columns and df_1min["volume"].notnull().any()
    vol_series = df_1min["volume"] if has_vol else df_1min["business"]

    vol_colors = [
        "rgba(0, 200, 83, 0.35)" if c >= o else "rgba(255, 23, 68, 0.35)"
        for o, c in zip(df_1min["open"], df_1min["close"])
    ]

    fig.add_trace(
        go.Bar(
            x=df_1min.index,
            y=vol_series,
            name="Volume (1m)",
            marker_color=vol_colors,
            showlegend=False,
            hovertemplate="<b>Volume 1m:</b> %{y:,.0f}<extra></extra>",
        ),
        row=2,
        col=1,
    )

    y_min = float(df_1min["low"].min())
    y_max = float(df_1min["high"].max())
    y_span = max(y_max - y_min, 1.0)

    groups = {}

    for tf in ["15min", "10min", "5min"]:
        visible = tf == "15min"
        groups[tf] = []

        b = per_timeframe[tf]
        b2 = b["b2_pivots"]
        b3 = b["b3_pivots"]
        regions = b["sideways_regions"]
        suppressed = b["b3_suppressed_pivots"]

        # B2 reference
        fig.add_trace(
            go.Scatter(
                x=[p["time"] for p in b2],
                y=[p["price"] for p in b2],
                mode="lines",
                line=dict(color=COLOR_B2, width=1.4, dash="dot"),
                name=f"B2 referência ({tf})",
                visible=visible,
            ),
            row=1,
            col=1,
        )
        groups[tf].append(len(fig.data) - 1)

        # SIDEWAYS regions
        fig.add_trace(
            go.Bar(
                x=[_midpoint(r["start"], r["end"]) for r in regions],
                y=[y_span] * len(regions),
                base=[y_min] * len(regions),
                width=[_duration_ms(r["start"], r["end"]) for r in regions],
                marker_color=COLOR_SIDEWAYS,
                marker_line_width=0,
                opacity=1.0,
                name=f"SIDEWAYS ({tf}) - {len(regions)}",
                visible=visible,
                customdata=[
                    [
                        r["start"], r["end"], r["duration_minutes"],
                        r["mean_er"], r["mean_slope_atr"],
                        r["range_points"], r["internal_b2_pivots"],
                    ]
                    for r in regions
                ],
                hovertemplate=(
                    f"<b>SIDEWAYS — {tf}</b><br>"
                    "Início: %{customdata[0]|%H:%M}<br>"
                    "Fim: %{customdata[1]|%H:%M}<br>"
                    "Duração: %{customdata[2]:.0f} min<br>"
                    "ER médio: %{customdata[3]:.3f}<br>"
                    "Slope/ATR: %{customdata[4]:.3f}<br>"
                    "Range: %{customdata[5]:.0f} pts<br>"
                    "Pivôs B2 internos: %{customdata[6]}"
                    "<extra></extra>"
                ),
            ),
            row=1,
            col=1,
        )
        groups[tf].append(len(fig.data) - 1)

        # B3 structural line, broken across SIDEWAYS.
        x_b3, y_b3 = _line_with_sideways_gaps(b3, regions)

        fig.add_trace(
            go.Scatter(
                x=x_b3,
                y=y_b3,
                mode="lines",
                line=dict(color=line_colors[tf], width=3.2),
                name=f"B3 Regime ({tf})",
                visible=visible,
            ),
            row=1,
            col=1,
        )
        groups[tf].append(len(fig.data) - 1)

        tops = [p for p in b3 if p["type"] == "TOP"]
        valleys = [p for p in b3 if p["type"] == "VALLEY"]

        fig.add_trace(
            go.Scatter(
                x=[p["time"] for p in tops],
                y=[p["price"] for p in tops],
                mode="markers",
                marker=dict(
                    symbol="triangle-up",
                    size=13,
                    color=COLOR_TOP,
                    line=dict(color="#FFFFFF", width=1.5),
                ),
                name=f"Topos B3 ({tf}) - {len(tops)}",
                visible=visible,
                hovertemplate=(
                    f"<b>▲ TOPO ESTRUTURAL B3 ({tf})</b><br>"
                    "%{x|%H:%M}<br>%{y:,.0f} pts<extra></extra>"
                ),
            ),
            row=1,
            col=1,
        )
        groups[tf].append(len(fig.data) - 1)

        fig.add_trace(
            go.Scatter(
                x=[p["time"] for p in valleys],
                y=[p["price"] for p in valleys],
                mode="markers",
                marker=dict(
                    symbol="triangle-down",
                    size=13,
                    color=COLOR_BOTTOM,
                    line=dict(color="#FFFFFF", width=1.5),
                ),
                name=f"Vales B3 ({tf}) - {len(valleys)}",
                visible=visible,
                hovertemplate=(
                    f"<b>▼ VALE ESTRUTURAL B3 ({tf})</b><br>"
                    "%{x|%H:%M}<br>%{y:,.0f} pts<extra></extra>"
                ),
            ),
            row=1,
            col=1,
        )
        groups[tf].append(len(fig.data) - 1)

        fig.add_trace(
            go.Scatter(
                x=[p["time"] for p in suppressed],
                y=[p["price"] for p in suppressed],
                mode="markers",
                marker=dict(
                    symbol="x",
                    size=10,
                    color=COLOR_SUPPRESSED,
                    line=dict(color="#FFFFFF", width=0.8),
                ),
                name=f"Pivôs suprimidos em SIDEWAYS ({tf}) - {len(suppressed)}",
                visible=visible,
                customdata=[
                    [p["type"], p["sideways_start"], p["sideways_end"]]
                    for p in suppressed
                ],
                hovertemplate=(
                    "<b>PIVÔ SUPRIMIDO — SIDEWAYS</b><br>"
                    "Tipo local: %{customdata[0]}<br>"
                    "Horário: %{x|%H:%M}<br>"
                    "Preço: %{y:,.0f}<br>"
                    "SIDEWAYS: %{customdata[1]|%H:%M} → %{customdata[2]|%H:%M}"
                    "<extra></extra>"
                ),
            ),
            row=1,
            col=1,
        )
        groups[tf].append(len(fig.data) - 1)

    amplitude = df_1min["high"].max() - df_1min["low"].min()

    def title_for(tf):
        if tf == "ALL":
            return (
                "<b>BovDB — B3 Regime — Todas as janelas</b><br>"
                f"<span style='color:#a0a0a0; font-size:13px;'>"
                f"{ticker} | {date} | "
                "SIDEWAYS sombreado; sem TOP/VALLEY estrutural interno"
                "</span>"
            )

        s = per_timeframe[tf]["summary"]
        return (
            f"<b>BovDB — B3 Regime — Janela {tf}</b><br>"
            f"<span style='color:#a0a0a0; font-size:13px;'>"
            f"{ticker} | {date} | Amplitude: {amplitude:,.0f} pts | "
            f"B2 pivôs={s['b2_pivots']} → B3 pivôs={s['b3_pivots']} | "
            f"SIDEWAYS={s['sideways_regions']} regiões / {s['sideways_minutes']:.0f} min | "
            f"ER≤{cfg.sideways_er_max:.2f}, "
            f"Slope/ATR≤{cfg.sideways_slope_atr_max:.2f}"
            "</span>"
        )

    n_traces = len(fig.data)

    def mask_for(tf):
        mask = [False] * n_traces
        mask[0] = True
        mask[1] = True

        if tf == "ALL":
            for w in ["15min", "10min", "5min"]:
                for idx in groups[w]:
                    mask[idx] = True
        else:
            for idx in groups[tf]:
                mask[idx] = True

        return mask

    timeframe_buttons = [
        dict(label="🟢 Janela 15m (Macro)", method="update",
             args=[{"visible": mask_for("15min")}, {"title.text": title_for("15min")}]),
        dict(label="🟡 Janela 10m (Médio)", method="update",
             args=[{"visible": mask_for("10min")}, {"title.text": title_for("10min")}]),
        dict(label="🟣 Janela 5m (Micro)", method="update",
             args=[{"visible": mask_for("5min")}, {"title.text": title_for("5min")}]),
        dict(label="⚡ Todas Sobrepostas", method="update",
             args=[{"visible": mask_for("ALL")}, {"title.text": title_for("ALL")}]),
    ]

    zoom_buttons = [
        dict(label="🔍 Abertura (09h - 12h)", method="relayout",
             args=[{"xaxis.range": [f"{date} 09:00:00", f"{date} 12:00:00"]}]),
        dict(label="🔍 Tarde (12h - 15h30)", method="relayout",
             args=[{"xaxis.range": [f"{date} 12:00:00", f"{date} 15:30:00"]}]),
        dict(label="🔍 Fechamento (15h30 - 18h30)", method="relayout",
             args=[{"xaxis.range": [f"{date} 15:30:00", f"{date} 18:35:00"]}]),
        dict(label="🔍 Dia Completo (09h - 18h30)", method="relayout",
             args=[{"xaxis.range": [f"{date} 09:00:00", f"{date} 18:35:00"]}]),
    ]

    fig.update_layout(
        title=dict(text=title_for("15min"), font=dict(size=18, color="#FFFFFF"), x=0.0, y=0.98),
        paper_bgcolor="#000000",
        plot_bgcolor="#000000",
        height=950,
        hovermode="x unified",
        barmode="overlay",
        updatemenus=[
            dict(
                type="buttons", direction="right",
                x=0.0, y=1.10, xanchor="left", yanchor="top",
                active=0, bgcolor="#121212", bordercolor="#2a2a2a",
                font=dict(color="#ffffff", size=11),
                buttons=timeframe_buttons,
            ),
            dict(
                type="buttons", direction="right",
                x=1.0, y=1.10, xanchor="right", yanchor="top",
                active=0, bgcolor="#121212", bordercolor="#2a2a2a",
                font=dict(color="#ffffff", size=11),
                buttons=zoom_buttons,
            ),
        ],
        legend=dict(
            orientation="h", yanchor="bottom", y=1.02,
            xanchor="center", x=0.5,
            bgcolor="rgba(0,0,0,0.7)", bordercolor="#222222",
            font=dict(size=11, color="#FFFFFF"),
        ),
        margin=dict(l=65, r=45, t=130, b=40),
    )

    fig.update_xaxes(
        range=[f"{date} 09:00:00", f"{date} 12:00:00"],
        rangeslider_visible=False,
        gridcolor="#151515",
        linecolor="#2a2a2a",
        tickcolor="#2a2a2a",
        tickfont=dict(color="#9e9e9e"),
    )

    fig.update_yaxes(
        title_text="Preço (pts)",
        title_font=dict(color="#e0e0e0", size=12),
        gridcolor="#151515",
        linecolor="#2a2a2a",
        tickcolor="#2a2a2a",
        tickfont=dict(color="#9e9e9e"),
        zeroline=False,
        row=1, col=1,
    )

    fig.update_yaxes(
        title_text="Volume",
        title_font=dict(color="#e0e0e0", size=11),
        gridcolor="#151515",
        linecolor="#2a2a2a",
        tickcolor="#2a2a2a",
        tickfont=dict(color="#757575"),
        zeroline=False,
        row=2, col=1,
    )

    return fig


# ============================================================================
# Runner
# ============================================================================

def run_regime_benchmark(df_1min, cfg=DEFAULT_CONFIG):
    per_timeframe = {}

    for tf in ["15min", "10min", "5min"]:
        topos, fundos, conf = detectar_topos_fundos(df_1min, macro_timeframe=tf)

        b0_pivots = pivots_from_b0(topos, fundos)
        b1_pivots, b1_removals = structural_filter_pivots(df_1min, b0_pivots, cfg=cfg)
        b2_pivots, b2_removals = structural_significance_filter(df_1min, b1_pivots, cfg=cfg)

        b2_labels = pivots_to_binary_trend_labels(df_1min, b2_pivots)

        sideways_features, sideways_regions = detect_sideways_regions(
            df_1min, tf, cfg=cfg, b2_pivots=b2_pivots
        )

        b3_pivots, b3_suppressed_pivots, b3_dominated_pivots = suppress_pivots_inside_sideways(
            b2_pivots, sideways_regions
        )

        b3_labels = build_three_class_regime_labels(
            df_1min, b2_labels, sideways_features, sideways_regions
        )

        summary = structural_summary(
            b0_pivots, b1_pivots, b2_pivots, b3_pivots,
            sideways_regions, b3_labels, df_1min
        )

        per_timeframe[tf] = {
            "topos": topos,
            "fundos": fundos,
            "conf": conf,
            "b0_pivots": b0_pivots,
            "b1_pivots": b1_pivots,
            "b2_pivots": b2_pivots,
            "b3_pivots": b3_pivots,
            "b1_removals": b1_removals,
            "b2_removals": b2_removals,
            "sideways_features": sideways_features,
            "sideways_regions": sideways_regions,
            "b3_suppressed_pivots": b3_suppressed_pivots,
            "b3_dominated_pivots": b3_dominated_pivots,
            "b2_labels": b2_labels,
            "b3_labels": b3_labels,
            "summary": summary,
        }

    return per_timeframe


def export_results(per_timeframe, output_dir, ticker, date):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    summaries = []

    for tf, b in per_timeframe.items():
        safe_tf = tf.replace("min", "m")

        pd.DataFrame(b["b3_pivots"]).to_csv(
            output_dir / f"b3_structural_pivots_{ticker}_{date}_{safe_tf}.csv",
            index=False,
        )

        pd.DataFrame(b["sideways_regions"]).to_csv(
            output_dir / f"b3_sideways_regions_{ticker}_{date}_{safe_tf}.csv",
            index=False,
        )

        pd.DataFrame(b["b3_suppressed_pivots"]).to_csv(
            output_dir / f"b3_pivots_suppressed_by_sideways_{ticker}_{date}_{safe_tf}.csv",
            index=False,
        )

        b["b3_labels"].to_csv(
            output_dir / f"b3_regime_labels_3class_{ticker}_{date}_{safe_tf}.csv",
            index=True,
            index_label="timestamp",
        )

        b["sideways_features"].to_csv(
            output_dir / f"b3_sideways_features_{ticker}_{date}_{safe_tf}.csv",
            index=True,
            index_label="timestamp",
        )

        summaries.append({"timeframe": tf, **b["summary"]})

    pd.DataFrame(summaries).to_csv(
        output_dir / f"b3_regime_summary_{ticker}_{date}.csv",
        index=False,
    )


# ============================================================================
# Synthetic test
# ============================================================================

def synthetic_self_test():
    idx = pd.date_range("2026-04-30 09:00:00", periods=150, freq="min")

    up = np.linspace(130000, 130700, 50)
    side = 130700 + 45 * np.sin(np.linspace(0, 12 * np.pi, 50))
    down = np.linspace(130700, 129900, 50)

    close = np.r_[up, side, down]
    open_ = np.r_[close[0], close[:-1]]

    df = pd.DataFrame(
        {
            "open": open_,
            "close": close,
            "high": np.maximum(open_, close) + 12,
            "low": np.minimum(open_, close) - 12,
            "volume": 1000,
            "business": 100,
        },
        index=idx,
    )

    features, regions = detect_sideways_regions(
        df, "5min", cfg=DEFAULT_CONFIG, b2_pivots=[]
    )

    assert regions, "B3 não detectou SIDEWAYS no sinal sintético"

    expected_start = idx[50]
    expected_end = idx[99]

    overlap = 0.0
    for r in regions:
        start = max(r["start"], expected_start)
        end = min(r["end"], expected_end)
        if start <= end:
            overlap += (end - start).total_seconds() / 60.0 + 1.0

    assert overlap >= 20, (overlap, regions)

    # Local pivots inside the synthetic sideways range.
    b2_pivots = [
        {"time": idx[25], "type": "TOP", "price": float(df["high"].iloc[25]), "close": float(df["close"].iloc[25])},
        {"time": idx[58], "type": "VALLEY", "price": float(df["low"].iloc[58]), "close": float(df["close"].iloc[58])},
        {"time": idx[68], "type": "TOP", "price": float(df["high"].iloc[68]), "close": float(df["close"].iloc[68])},
        {"time": idx[78], "type": "VALLEY", "price": float(df["low"].iloc[78]), "close": float(df["close"].iloc[78])},
        {"time": idx[88], "type": "TOP", "price": float(df["high"].iloc[88]), "close": float(df["close"].iloc[88])},
        {"time": idx[125], "type": "VALLEY", "price": float(df["low"].iloc[125]), "close": float(df["close"].iloc[125])},
    ]

    b3_pivots, suppressed, _ = suppress_pivots_inside_sideways(b2_pivots, regions)

    assert all(not timestamp_in_sideways(p["time"], regions) for p in b3_pivots)
    assert len(suppressed) >= 2

    b2_labels = pd.DataFrame(index=df.index)
    b2_labels["trend_label"] = pd.Series(1, index=df.index, dtype="Int64")
    b2_labels.loc[df.index >= idx[100], "trend_label"] = 0

    b3_labels = build_three_class_regime_labels(
        df, b2_labels, features, regions
    )

    assert (b3_labels["trend_label"] == SIDEWAYS_3C).any()

    return {
        "sideways_regions": len(regions),
        "sideways_overlap_minutes": round(overlap, 2),
        "b2_pivots_before": len(b2_pivots),
        "b3_pivots_after": len(b3_pivots),
        "suppressed_inside_sideways": len(suppressed),
        "has_down": bool((b3_labels["trend_label"] == DOWNTREND_3C).any()),
        "has_sideways": bool((b3_labels["trend_label"] == SIDEWAYS_3C).any()),
        "has_up": bool((b3_labels["trend_label"] == UPTREND_3C).any()),
    }


if __name__ == "__main__":
    project_dir = Path(__file__).resolve().parents[1]
    db_path = project_dir / "data" / "bovdb-v3.1-internal.1.sqlite"

    ticker = "WINM26"
    date = "2026-04-30"

    output_dir = project_dir / "results" / "b3_regime"
    html_dir = project_dir / "html"

    output_dir.mkdir(parents=True, exist_ok=True)
    html_dir.mkdir(parents=True, exist_ok=True)

    print(f"Carregando {ticker} — {date}...")
    df_1min = load_win_data(db_path, ticker=ticker, date=date)

    print("Executando B0 -> B1 -> B2 -> B3 Regime...")
    results = run_regime_benchmark(df_1min, cfg=DEFAULT_CONFIG)

    for tf in ["15min", "10min", "5min"]:
        s = results[tf]["summary"]
        print(
            f"{tf:6s} | "
            f"B0={s['b0_pivots']:2d} -> "
            f"B1={s['b1_pivots']:2d} -> "
            f"B2={s['b2_pivots']:2d} -> "
            f"B3={s['b3_pivots']:2d} | "
            f"SIDEWAYS={s['sideways_regions']:2d} regiões / "
            f"{s['sideways_minutes']:.0f} min | "
            f"DOWN={s['down_candles']:3d} | "
            f"SIDE={s['sideways_candles']:3d} | "
            f"UP={s['up_candles']:3d}"
        )

    export_results(results, output_dir, ticker, date)

    fig = build_comparison_dashboard(
        df_1min, results, ticker=ticker, date=date, cfg=DEFAULT_CONFIG
    )

    output_html = html_dir / f"b3_regime_{ticker}_{date}.html"
    fig.write_html(str(output_html))

    print(f"Dashboard: {output_html}")
    print(f"Resultados: {output_dir}")
