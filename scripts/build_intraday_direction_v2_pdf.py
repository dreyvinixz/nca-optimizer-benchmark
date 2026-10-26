#!/usr/bin/env python3
"""Build the v2 intraday direction study report PDF from saved summaries."""
from pathlib import Path
from xml.sax.saxutils import escape

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (Image, KeepTogether, PageBreak, Paragraph,
                                SimpleDocTemplate, Spacer, Table, TableStyle)


ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
CHARTS = ROOT / "tmp" / "pdfs"
OUTPUT = ROOT / "output" / "pdf" / "relatorio_previsao_direcional_intradiaria_v2.pdf"
NAVY = colors.HexColor("#17324D")
TEAL = colors.HexColor("#117C78")
ORANGE = colors.HexColor("#E78335")
PALE = colors.HexColor("#EFF5F7")
MID = colors.HexColor("#5A6B78")
INK = colors.HexColor("#1E2933")
GRID = colors.HexColor("#D6E0E5")


def load_inputs():
    summary = pd.read_csv(REPORTS / "intraday_direction_v2_selection_summary.csv")
    stability = pd.read_csv(REPORTS / "intraday_direction_v2_selection_stability.csv")
    correlations = pd.read_csv(REPORTS / "intraday_direction_v2_selection_rank_correlations.csv")
    audit = (ROOT / "reports" / "intraday_direction_v2_data_audit.md").read_text(encoding="utf-8")
    manifest = __import__("json").loads((ROOT / "data" / "derived" / "intraday_direction_v2_features.manifest.json").read_text(encoding="utf-8"))
    config = __import__("yaml").safe_load((ROOT / "config" / "intraday_direction_v2.yaml").read_text(encoding="utf-8"))
    return summary, stability, correlations, manifest, config


def make_charts(summary, stability, correlations):
    CHARTS.mkdir(parents=True, exist_ok=True)
    palette = {"majority_prevalence": "#8798A5", "causal_5m_momentum": "#E78335",
               "logistic_regression": "#17324D", "hist_gradient_boosting": "#117C78"}
    labels = {"majority_prevalence": "Prevalência do treino",
              "causal_5m_momentum": "Momentum causal 5m",
              "logistic_regression": "Logística - todas as features",
              "hist_gradient_boosting": "HGB - todas as features"}
    pooled = summary[summary.root.eq("ALL")].copy()
    selected = pooled[((pooled.top_k.astype(str) == "all") &
                       (pooled.selection_method == "mutual_information") &
                       pooled.model.isin(["logistic_regression", "hist_gradient_boosting"])) |
                      ((pooled.top_k.astype(str) == "none") &
                       pooled.model.isin(["majority_prevalence", "causal_5m_momentum"]))]
    by_model = selected.groupby(["horizon", "model"], as_index=False).agg(
        mcc=("mcc_mean", "mean"), mcc_fold_sd=("mcc_sd", "mean"),
        balanced_accuracy=("balanced_accuracy_mean", "mean"),
        roc_auc=("roc_auc_mean", "mean"), pr_auc=("pr_auc_mean", "mean"),
    )
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.0))
    x = np.arange(3)
    width = 0.19
    models = ["majority_prevalence", "causal_5m_momentum", "logistic_regression", "hist_gradient_boosting"]
    for j, model in enumerate(models):
        dat = by_model[by_model.model.eq(model)].set_index("horizon")
        vals_mcc = [dat.loc[h, "mcc"] for h in (5, 15, 30)]
        vals_auc = [dat.loc[h, "roc_auc"] for h in (5, 15, 30)]
        axes[0].bar(x + (j - 1.5) * width, vals_mcc, width, color=palette[model], label=labels[model])
        axes[1].bar(x + (j - 1.5) * width, vals_auc, width, color=palette[model], label=labels[model])
    for ax, title, ylabel, baseline in [
        (axes[0], "MCC médio por horizonte", "MCC", 0.0),
        (axes[1], "ROC-AUC médio por horizonte", "ROC-AUC", 0.5),
    ]:
        ax.axhline(baseline, color="#71808A", linestyle="--", linewidth=1)
        ax.set_title(title, fontsize=11, fontweight="bold", color="#17324D")
        ax.set_ylabel(ylabel, fontsize=9)
        ax.set_xticks(x, ["5 min", "15 min", "30 min"])
        ax.grid(axis="y", color="#D6E0E5", linewidth=0.7)
        ax.set_axisbelow(True)
        ax.spines[["top", "right", "left"]].set_visible(False)
        ax.tick_params(axis="both", labelsize=8, length=0)
    axes[0].legend(loc="lower center", bbox_to_anchor=(1.02, -0.34), ncol=2,
                   frameon=False, fontsize=7)
    fig.tight_layout(rect=(0, 0.14, 1, 1))
    performance_chart = CHARTS / "v2_performance.png"
    fig.savefig(performance_chart, dpi=190, bbox_inches="tight", facecolor="white")
    plt.close(fig)

    pairs = correlations.groupby(["method_a", "method_b"], as_index=False).spearman_rank_correlation.mean()
    pair_labels = [f"{r.method_a.replace('_', ' ')} x {r.method_b.replace('_', ' ')}" for r in pairs.itertuples()]
    fig, ax = plt.subplots(figsize=(8.8, 3.2))
    colors_ = ["#117C78" if v >= 0.2 else "#E78335" for v in pairs.spearman_rank_correlation]
    ax.barh(pair_labels, pairs.spearman_rank_correlation, color=colors_, height=0.55)
    ax.axvline(0, color="#71808A", linewidth=0.8)
    ax.set_xlim(-0.1, 0.4)
    ax.set_xlabel("Correlação de Spearman dos rankings", fontsize=9)
    ax.set_title("Concordância média entre métodos", fontsize=11, fontweight="bold", color="#17324D")
    ax.grid(axis="x", color="#D6E0E5", linewidth=0.7)
    ax.set_axisbelow(True)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.tick_params(axis="both", labelsize=8, length=0)
    fig.tight_layout()
    rank_chart = CHARTS / "v2_rank_agreement.png"
    fig.savefig(rank_chart, dpi=190, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return performance_chart, rank_chart


def register_fonts():
    font_dir = Path("C:/Windows/Fonts")
    pdfmetrics.registerFont(TTFont("ArialV2", str(font_dir / "arial.ttf")))
    pdfmetrics.registerFont(TTFont("ArialV2-Bold", str(font_dir / "arialbd.ttf")))
    pdfmetrics.registerFont(TTFont("ArialV2-Italic", str(font_dir / "ariali.ttf")))
    pdfmetrics.registerFontFamily("ArialV2", normal="ArialV2", bold="ArialV2-Bold",
                                  italic="ArialV2-Italic", boldItalic="ArialV2-Bold")


def build_pdf():
    summary, stability, correlations, manifest, config = load_inputs()
    performance_chart, rank_chart = make_charts(summary, stability, correlations)
    register_fonts()
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="CoverTitleV2", fontName="ArialV2-Bold", fontSize=24,
                              leading=29, textColor=NAVY, alignment=TA_LEFT, spaceAfter=12))
    styles.add(ParagraphStyle(name="DeckV2", fontName="ArialV2", fontSize=12, leading=17,
                              textColor=MID, spaceAfter=12))
    styles.add(ParagraphStyle(name="H1V2", fontName="ArialV2-Bold", fontSize=16, leading=20,
                              textColor=NAVY, spaceBefore=4, spaceAfter=9, keepWithNext=True))
    styles.add(ParagraphStyle(name="H2V2", fontName="ArialV2-Bold", fontSize=11, leading=14,
                              textColor=TEAL, spaceBefore=8, spaceAfter=5, keepWithNext=True))
    styles.add(ParagraphStyle(name="BodyV2", fontName="ArialV2", fontSize=9.2, leading=13.4,
                              textColor=INK, spaceAfter=6))
    styles.add(ParagraphStyle(name="SmallV2", fontName="ArialV2", fontSize=7.4, leading=10,
                              textColor=MID, spaceAfter=4))
    styles.add(ParagraphStyle(name="CalloutV2", fontName="ArialV2-Bold", fontSize=10,
                              leading=14, textColor=NAVY, backColor=PALE, borderColor=TEAL,
                              borderWidth=0.6, borderPadding=8, spaceBefore=5, spaceAfter=9))

    summary_all = summary[summary.root.eq("ALL")]
    selected = summary_all[((summary_all.top_k.astype(str) == "all") &
                            (summary_all.selection_method == "mutual_information") &
                            summary_all.model.isin(["logistic_regression", "hist_gradient_boosting"])) |
                           ((summary_all.top_k.astype(str) == "none") &
                            summary_all.model.isin(["majority_prevalence", "causal_5m_momentum"]))]
    performance = selected.groupby(["horizon", "model"], as_index=False).agg(
        mcc=("mcc_mean", "mean"), mcc_sd=("mcc_sd", "mean"),
        bacc=("balanced_accuracy_mean", "mean"), macro_f1=("macro_f1_mean", "mean"),
        roc_auc=("roc_auc_mean", "mean"), pr_auc=("pr_auc_mean", "mean"),
        brier=("brier_mean", "mean"),
    )
    model_labels = {"majority_prevalence": "Prevalencia treino", "causal_5m_momentum": "Momentum 5m",
                    "logistic_regression": "Logística, 101 features", "hist_gradient_boosting": "HGB, 101 features"}

    selected_best = summary_all.sort_values("mcc_mean", ascending=False).groupby(["horizon", "band"], as_index=False).first()
    corr_summary = correlations.groupby(["method_a", "method_b"], as_index=False).spearman_rank_correlation.mean()
    stability_summary = stability.groupby(["method", "feature"], as_index=False).agg(
        mean_rank=("mean_rank", "mean"), top10=("top10_frequency", "mean"),
        top20=("top20_frequency", "mean"),
    )
    feature_names = {"mutual_information": "Informação mútua", "l1_logistic": "Logística L1",
                     "inner_temporal_permutation": "Permutação temporal interna"}

    story = []
    story.append(Spacer(1, 24 * mm))
    story.append(Paragraph("Previsão direcional<br/>intradiária", styles["CoverTitleV2"]))
    story.append(Paragraph("Baseline com indicadores OHLCV e seleção de features em WIN e IND", styles["DeckV2"]))
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("Relatório técnico de desenvolvimento - v2", styles["H2V2"]))
    story.append(Paragraph("Período disponível: janeiro a junho de 2026 | Dados: candles de um minuto | Execução: 5 folds temporais expanding", styles["BodyV2"]))
    story.append(Spacer(1, 7 * mm))
    story.append(Paragraph("Resultado central: os rankings dos três métodos concordam pouco e a performance pooled permanece próxima do acaso. A regressão logística também apresentou avisos de não convergência em alguns ajustes.", styles["CalloutV2"]))
    story.append(Spacer(1, 8 * mm))
    story.append(Paragraph("Este relatório descreve uma baseline exploratória. Todo o período disponível foi usado em desenvolvimento; o teste histórico aberto no estudo B0 não é um teste independente para esta hipótese.", styles["SmallV2"]))
    story.append(PageBreak())

    story.append(Paragraph("1. Introdução", styles["H1V2"]))
    story.append(Paragraph("O estudo amplia a baseline anterior para prever a direção do retorno futuro de preços. A pergunta é se um conjunto mais amplo de indicadores causais melhora a previsão binária em diferentes horizontes e faixas do pregão, e quais features permanecem bem ranqueadas quando a seleção respeita a ordem temporal.", styles["BodyV2"]))
    story.append(Paragraph("A previsão é emitida após o fechamento do candle atual de um minuto. O alvo é o sinal do retorno logarítmico entre o fechamento atual e o fechamento após 5, 15 ou 30 barras observadas. O trabalho não prevê os rótulos B0 e não interpreta esses rótulos como verdade-terreno.", styles["BodyV2"]))
    story.append(Paragraph("As faixas 09:00-12:00, 12:00-15:00 e 15:00-18:00 são cortes definidos para esta análise dentro da janela local disponível. Elas não representam uma declaração sobre horários oficiais da bolsa.", styles["BodyV2"]))
    story.append(Paragraph("2. Dados e construção dos alvos", styles["H1V2"]))
    story.append(Paragraph(f"A extração somente leitura do SQLite contém {manifest['rows']:,} candles de {manifest['dates']} pregões: WIN ({119670:,} linhas) e IND ({62304:,}). A janela observada é 09:00-17:59. O cache Parquet tem {manifest['output_bytes'] / 1_000_000:.1f} MB e sua geração levou {manifest['runtime_seconds']:.2f} segundos.", styles["BodyV2"]))
    story.append(Paragraph("Para cada horizonte h, o alvo é 1 quando log(close[t+h] / close[t]) > 0 e 0 quando o retorno é zero ou negativo. Uma linha é excluída se faltar qualquer minuto intermediário ou se o deslocamento cruzar ticker, data ou segmento contínuo. Não há banda neutra nesta versão.", styles["BodyV2"]))
    table_data = [["Horizonte", "Alvos válidos", "Prevalência de alta", "Early", "Middle", "Late"]]
    for h in (5, 15, 30):
        s = manifest["target_summary"][str(h)]
        table_data.append([f"{h} min", f"{s['valid']:,}", f"{s['up_prevalence']:.3f}",
                           f"{s['by_band']['early']['n']:,}", f"{s['by_band']['middle']['n']:,}", f"{s['by_band']['late']['n']:,}"])
    story.append(make_table(table_data, [26, 33, 37, 25, 25, 25]))
    story.append(Paragraph(f"O conjunto inclui 101 indicadores; {manifest['feature_rows_complete']:,} linhas ({manifest['feature_rows_complete'] / manifest['rows']:.1%}) têm todas as features após o aquecimento completo. A auditoria confirmou chave única, sinal do retorno futuro e ausência de campos B4/futuros nas entradas.", styles["SmallV2"]))
    story.append(PageBreak())

    story.append(Paragraph("3. Metodologia", styles["H1V2"]))
    story.append(Paragraph("3.1 Indicadores", styles["H2V2"]))
    families = [
        ["Família", "Conteúdo", "N"],
        ["Retorno e momentum", "Retornos log em 1, 2, 3, 5, 10, 15 e 30 min", "7"],
        ["Geometria do candle", "Corpo, amplitude, pavios e posição do fechamento", "5"],
        ["Médias e MACD", "SMA/EMA 5-30; MACD 12/26, sinal e histograma", "13"],
        ["Osciladores", "RSI 7/14/28; estocástico %K/%D 14/28", "7"],
        ["Amplitude/direção", "ATR 5/14/30; +DI, -DI e ADX 14/28", "9"],
        ["Volatilidade", "Volatilidade realizada e semivolatilidade +/- 5-30", "15"],
        ["Bandas/canais", "Bollinger %B/largura 20/30; Donchian 10/20/30", "10"],
        ["Atividade", "Volume, negócios e quantidade: log, surpresa, robusto e z-score", "27"],
        ["Acumulados e horário", "Retorno/amplitude e atividade no pregão; hora seno/cosseno", "8"],
        ["Total", "Features causais; reinício em gap, contrato e pregão", "101"],
    ]
    story.append(make_table(families, [33, 113, 14], font_size=7.2))
    story.append(Paragraph("Features usam o candle atual já fechado e o passado. Não há minutos sintéticos, forward-fill nem imputação. A janela rolling exige aquecimento completo. Volume, negócios e quantidade são transformados por log e comparados a estatísticas móveis retrospectivas.", styles["BodyV2"]))
    story.append(Paragraph("3.2 Seleção de features e avaliação", styles["H2V2"]))
    story.append(Paragraph("Três seletores são ajustados dentro do treino externo: (1) informação mútua univariada; (2) magnitude dos coeficientes de regressão logística L1 com escala aprendida no treino; e (3) importância por permutação em balanced accuracy, com HistGradientBoosting ajustado no treino interno e medido nos 10 pregões seguintes. A permutação usa até 2.000 observações e três repetições por feature.", styles["BodyV2"]))
    story.append(Paragraph("Cada ranking é usado para selecionar top-10, top-20 e todas as 101 features. Os modelos avaliadores são regressão logística e HistGradientBoosting. Referências sem seleção: prevalência majoritária do treino e momentum causal dado pelo retorno observado de 5 minutos.", styles["BodyV2"]))
    story.append(Paragraph("A validação usa cinco origens expanding: 69 pregões iniciais e blocos externos de 10 pregões. A parte interna mais recente de 10 pregões é reservada ao ranking por permutação. Métricas principais: MCC, balanced accuracy e macro-F1; complementares: acurácia, precisão/recall por classe, ROC-AUC, PR-AUC, Brier, log-loss e matriz de confusão. Folds temporais são dependentes; o desvio entre folds é descritivo.", styles["BodyV2"]))
    story.append(Paragraph("Os resultados por WIN e IND desagregam as mesmas previsões do modelo conjunto. Não são modelos treinados separadamente para cada raiz.", styles["BodyV2"]))
    story.append(PageBreak())

    story.append(Paragraph("4. Resultados", styles["H1V2"]))
    story.append(Paragraph("4.1 Baselines pooled, média simples das três faixas", styles["H2V2"]))
    story.append(Image(str(performance_chart), width=174 * mm, height=65 * mm))
    perf_table = [["Horizonte", "Modelo", "MCC", "DP fold MCC", "Bal. acc.", "ROC-AUC", "PR-AUC"]]
    for h in (5, 15, 30):
        for model in ("majority_prevalence", "causal_5m_momentum", "logistic_regression", "hist_gradient_boosting"):
            r = performance[(performance.horizon == h) & (performance.model == model)].iloc[0]
            perf_table.append([f"{h} min", model_labels[model], f"{r.mcc:.3f}", f"{r.mcc_sd:.3f}",
                               f"{r.bacc:.3f}", f"{r.roc_auc:.3f}", f"{r.pr_auc:.3f}"])
    story.append(make_table(perf_table, [19, 45, 19, 24, 22, 20, 20], font_size=6.8))
    story.append(Paragraph("A escolha de todas as features não depende do ranking: os três seletores geram o mesmo conjunto para K=all. Os números acima são médias simples entre faixas e configurações como descrito; não são estimativas de um modelo final selecionado.", styles["SmallV2"]))
    story.append(Paragraph("4.2 Melhores combinações por horizonte e faixa", styles["H2V2"]))
    best_table = [["Horizonte", "Faixa", "Método", "K", "Modelo", "MCC ± DP", "ROC-AUC", "PR-AUC"]]
    for r in selected_best.sort_values(["horizon", "band"]).itertuples():
        method_label = {"mutual_information": "informação mútua", "l1_logistic": "L1",
                        "inner_temporal_permutation": "permutação"}.get(r.selection_method, r.selection_method)
        best_table.append([f"{r.horizon} min", r.band, method_label,
                           str(r.top_k), "Logística" if r.model == "logistic_regression" else "HGB",
                           f"{r.mcc_mean:.3f} ± {r.mcc_sd:.3f}", f"{r.roc_auc_mean:.3f}", f"{r.pr_auc_mean:.3f}"])
    story.append(make_table(best_table, [21, 19, 36, 12, 22, 26, 20, 20], font_size=6.6))
    story.append(Paragraph("Esses máximos foram escolhidos depois de comparar muitos métodos, K, modelos e faixas nos mesmos folds. São apenas exploratórios e tendem a superestimar a melhor configuração.", styles["SmallV2"]))
    story.append(PageBreak())

    story.append(Paragraph("4.3 Rankings e estabilidade", styles["H1V2"]))
    story.append(Image(str(rank_chart), width=155 * mm, height=57 * mm))
    corr_table = [["Método A", "Método B", "Spearman médio"]]
    for r in corr_summary.itertuples():
        corr_table.append([feature_names.get(r.method_a, r.method_a), feature_names.get(r.method_b, r.method_b),
                           f"{r.spearman_rank_correlation:.3f}"])
    story.append(make_table(corr_table, [63, 63, 36]))
    story.append(Paragraph("A concordância é baixa: informação mútua vs. L1 = 0,240; informação mútua vs. permutação = 0,114; L1 vs. permutação = 0,054. Portanto, os métodos não identificam um ranking consensual.", styles["BodyV2"]))
    top_table = [["Método", "Features mais bem ranqueadas (média entre 9 tarefas)", "Freq. top-10"]]
    for method in feature_names:
        part = stability_summary[stability_summary.method.eq(method)].sort_values("mean_rank").head(5)
        names = ", ".join(part.feature.tolist())
        freq = ", ".join(f"{v:.0%}" for v in part.top10.tolist())
        top_table.append([feature_names[method], names, freq])
    story.append(make_table(top_table, [40, 101, 25], font_size=6.8))
    story.append(Paragraph("A informação mútua coloca `session_range_so_far` e indicadores de semivolatilidade repetidamente no topo. A estabilidade é de ordenação, não prova de utilidade causal; o resultado depende do horizonte/faixa e da definição do alvo.", styles["SmallV2"]))

    story.append(PageBreak())
    story.append(Paragraph("5. Limitações e diagnóstico", styles["H1V2"]))
    limitations = [
        "As métricas pooled ficam próximas da referência majoritária; momentum causal é negativo. Nenhum top-K mostra vantagem estável nos três horizontes.",
        "A regressão logística emitiu avisos de não convergência no limite de 400 iterações em alguns ajustes. Seus números são provisórios e precisam de nova execução com mais iterações e registro explícito da convergência por fold.",
        "Há oscilações por raiz e faixa; os recortes são menores e as métricas devem ser lidas com cobertura, prevalência e matriz de confusão.",
        "Não foi medido gap treino-validação nesta execução. A variação entre os cinco folds é descritiva, não um teste formal de sobreajuste nem um intervalo de confiança independente.",
        "Os dados disponíveis vão até junho de 2026 e foram usados em desenvolvimento. O teste B0 aberto anteriormente não é holdout para esta nova hipótese. Não há avaliação de execução, custos ou rentabilidade.",
    ]
    for item in limitations:
        story.append(Paragraph("• " + item, styles["BodyV2"]))
    story.append(Paragraph("6. Conclusão e próximos passos", styles["H1V2"]))
    story.append(Paragraph("O pipeline causal com 101 indicadores e três seletores temporais está implementado e auditado. O ranking de informação mútua é mais estável em amplitude e semivolatilidade, mas a baixa concordância global e a performance pooled perto do acaso não sustentam uma feature set universal ou uma vantagem preditiva estável.", styles["BodyV2"]))
    story.append(Paragraph("Antes de uma conclusão confirmatória: (1) corrigir e registrar convergência da regressão logística; (2) medir gap treino-validação nos finalistas; (3) congelar protocolo antes de obter e abrir um período futuro intocado; (4) avaliar custos de execução em estudo separado.", styles["BodyV2"]))
    story.append(Paragraph(f"Proveniência: hash SHA-256 do SQLite {manifest['source_sha256']}. Configuração, auditoria, CSVs e código de geração estão no repositório. O Parquet permanece em data/derived e não é versionado.", styles["SmallV2"]))

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(OUTPUT), pagesize=A4, rightMargin=17 * mm, leftMargin=17 * mm,
                            topMargin=17 * mm, bottomMargin=18 * mm,
                            title="Previsao direcional intradiaria - Baseline v2",
                            subject="Indicadores e selecao de features em futuros WIN e IND")
    doc.build(story, onFirstPage=draw_page, onLaterPages=draw_page)
    print(OUTPUT)


def make_table(data, widths_mm, font_size=7.4):
    header_style = ParagraphStyle(name=f"TableHeader{font_size}", fontName="ArialV2-Bold",
                                  fontSize=font_size, leading=font_size + 2,
                                  textColor=colors.white)
    body_style = ParagraphStyle(name=f"TableBody{font_size}", fontName="ArialV2",
                                fontSize=font_size, leading=font_size + 2,
                                textColor=INK)
    wrapped = [[Paragraph(escape(str(cell)), header_style if row_i == 0 else body_style)
                for cell in row] for row_i, row in enumerate(data)]
    table = Table(wrapped, colWidths=[w * mm for w in widths_mm], repeatRows=1, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "ArialV2-Bold"),
        ("FONTNAME", (0, 1), (-1, -1), "ArialV2"),
        ("FONTSIZE", (0, 0), (-1, -1), font_size),
        ("LEADING", (0, 0), (-1, -1), font_size + 2),
        ("GRID", (0, 0), (-1, -1), 0.35, GRID),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, PALE]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return table


def draw_page(canvas, doc):
    canvas.saveState()
    width, height = A4
    canvas.setStrokeColor(GRID)
    canvas.setLineWidth(0.5)
    if doc.page > 1:
        canvas.line(17 * mm, height - 12 * mm, width - 17 * mm, height - 12 * mm)
        canvas.setFont("ArialV2", 7)
        canvas.setFillColor(MID)
        canvas.drawString(17 * mm, height - 9 * mm, "Previsão direcional intradiária - Baseline v2")
    canvas.line(17 * mm, 13 * mm, width - 17 * mm, 13 * mm)
    canvas.setFont("ArialV2", 7)
    canvas.setFillColor(MID)
    canvas.drawString(17 * mm, 8 * mm, "Relatório de desenvolvimento | 26 outubro 2026")
    canvas.drawRightString(width - 17 * mm, 8 * mm, f"{doc.page}")
    canvas.restoreState()


if __name__ == "__main__":
    build_pdf()
