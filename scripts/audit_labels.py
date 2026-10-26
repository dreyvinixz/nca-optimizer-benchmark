#!/usr/bin/env python3
"""Read-only B4 audit; SQL performs the large scans, Python aggregates small results."""
import argparse
import csv
import hashlib
import os
import re
import sqlite3
from collections import defaultdict
from pathlib import Path


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(8 * 1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def ro(path):
    return sqlite3.connect(path.resolve().as_uri() + '?mode=ro', uri=True)


def roots_from_yaml(path):
    lines = path.read_text(encoding='utf-8-sig').splitlines()
    start = next(i for i, x in enumerate(lines) if re.match(r'^\s{2}future_roots:\s*$', x))
    roots = []
    for line in lines[start + 1:]:
        if re.match(r'^\s{2}\S', line):
            break
        m = re.match(r'^\s{4,}-\s+([A-Z0-9]+)\s*$', line)
        if m:
            roots.append(m.group(1))
    if not roots:
        raise ValueError(f'No future_roots in {path}')
    return roots


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--label-db', type=Path, default=Path(os.getenv('BOVDB_B4_DB', 'data/bovdb-labels-B4-v1.sqlite')))
    ap.add_argument('--source-db', type=Path, default=Path(os.getenv('BOVDB_SOURCE_DB', 'data/bovdb-v3.1-internal.2.sqlite')))
    external_root = Path('/mnt/c/mysystems/services/bovdb') if os.name != 'nt' else Path(r'C:\mysystems\services\bovdb')
    ap.add_argument('--universe-config', type=Path, default=Path(os.getenv('BOVDB_UNIVERSE_CONFIG', str(external_root / 'bovdb-pipeline/config/v3_1_universe.yaml'))))
    ap.add_argument('--manifest', type=Path, default=Path(os.getenv('BOVDB_B4_MANIFEST', str(external_root / 'bovdb-pipeline/rotulos/data/bovdb-labels-B4-v1.manifest.json'))))
    ap.add_argument('--report', type=Path, default=Path('reports/label_audit.md'))
    ap.add_argument('--session-csv', type=Path, default=Path('reports/label_audit_by_root_session.csv'))
    a = ap.parse_args()
    roots = roots_from_yaml(a.universe_config)
    labels, source = ro(a.label_db), ro(a.source_db)
    meta_cur = labels.execute('SELECT * FROM label_run')
    meta = dict(zip([x[0] for x in meta_cur.description], meta_cur.fetchone()))
    print('Loaded label metadata; scanning per-session distributions', flush=True)

    # Window functions compute one-minute transitions in SQLite, avoiding millions
    # of Python row operations. Results below are only a few thousand sessions.
    minute = "(CAST(substr(time,1,2) AS INTEGER)*60 + CAST(substr(time,4,2) AS INTEGER))"
    by_tf = {}
    by_contract = {}
    for tf in ('5m', '10m', '15m'):
        table = f'trend_{tf}'
        sql = f'''WITH ordered AS (
          SELECT ticker,date,time,trend_label,{minute} AS minute,
                 LAG(trend_label) OVER (PARTITION BY id_ticker,date ORDER BY time) AS prev_label,
                 LAG({minute}) OVER (PARTITION BY id_ticker,date ORDER BY time) AS prev_minute
          FROM {table}
        )
        SELECT ticker,date,COUNT(*),
          SUM(trend_label IS NOT NULL),SUM(trend_label IS NULL),
          SUM(trend_label=1),SUM(trend_label=0),
          SUM(CASE WHEN trend_label IS NOT NULL AND prev_label IS NOT NULL AND minute-prev_minute=1 THEN 1 ELSE 0 END),
          SUM(CASE WHEN trend_label IS NOT NULL AND prev_label IS NOT NULL AND minute-prev_minute=1 AND trend_label!=prev_label THEN 1 ELSE 0 END),
          SUM(CASE WHEN prev_minute IS NOT NULL AND minute-prev_minute>1 THEN 1 ELSE 0 END),
          SUM(CASE WHEN prev_minute IS NOT NULL AND minute-prev_minute>1 THEN minute-prev_minute-1 ELSE 0 END),
          SUM(CASE WHEN trend_label IS NOT NULL AND (prev_label IS NULL OR minute-prev_minute!=1 OR trend_label!=prev_label) THEN 1 ELSE 0 END)
        FROM ordered GROUP BY ticker,date ORDER BY ticker,date'''
        rows = labels.execute(sql).fetchall()
        grouped = {}
        contracts = {}
        for ticker, day, n, valid, nulls, up, down, trans, changes, gaps, missing, runs in rows:
            root = next((r for r in roots if ticker.startswith(r)), None)
            c = contracts.setdefault(ticker, {'days': 0, 'rows': 0, 'valid': 0, 'nulls': 0, 'up': 0, 'down': 0, 'first': day, 'last': day})
            c['days'] += 1; c['rows'] += int(n); c['valid'] += int(valid or 0)
            c['nulls'] += int(nulls or 0); c['up'] += int(up or 0); c['down'] += int(down or 0)
            c['first'] = min(c['first'], day); c['last'] = max(c['last'], day)
            if root:
                s = grouped.setdefault((root, day), [0] * 12)
                vals = (1, n, valid, nulls, up, down, trans, changes, gaps, missing, runs, valid)
                for i, v in enumerate(vals):
                    s[i] += int(v or 0)
        by_tf[tf] = grouped
        by_contract[tf] = contracts
        print(f'  {tf}: {len(rows)} ticker-sessions summarized', flush=True)

    # Aggregate alignment and vote/mean checks inside SQLite as well.
    print('Scanning cross-timeframe agreement', flush=True)
    agree_sql = '''SELECT a.ticker,a.date,COUNT(*),
      SUM(a.trend_label IS NOT NULL AND b.trend_label IS NOT NULL AND c.trend_label IS NOT NULL),
      SUM(a.trend_label IS NOT NULL AND b.trend_label IS NOT NULL AND c.trend_label IS NOT NULL AND a.trend_label=b.trend_label AND b.trend_label=c.trend_label),
      SUM(a.trend_label IS NOT NULL AND b.trend_label IS NOT NULL AND c.trend_label IS NOT NULL AND m.trend_label=CAST((a.trend_label+b.trend_label+c.trend_label)>=2 AS INTEGER)),
      SUM(a.trend_label IS NOT NULL AND b.trend_label IS NOT NULL AND c.trend_label IS NOT NULL AND (m.trend_label IS NULL OR m.trend_label!=CAST((a.trend_label+b.trend_label+c.trend_label)>=2 AS INTEGER))),
      SUM(a.trend_label IS NOT NULL AND b.trend_label IS NOT NULL AND c.trend_label IS NOT NULL AND (m.mean_score IS NULL OR abs(m.mean_score-(a.trend_label+b.trend_label+c.trend_label)/3.0)>0.000000001)),
      SUM(a.trend_label IS NOT NULL AND b.trend_label IS NOT NULL AND a.trend_label=b.trend_label),
      SUM(a.trend_label IS NOT NULL AND b.trend_label IS NOT NULL),
      SUM(a.trend_label IS NOT NULL AND c.trend_label IS NOT NULL AND a.trend_label=c.trend_label),
      SUM(a.trend_label IS NOT NULL AND c.trend_label IS NOT NULL),
      SUM(b.trend_label IS NOT NULL AND c.trend_label IS NOT NULL AND b.trend_label=c.trend_label),
      SUM(b.trend_label IS NOT NULL AND c.trend_label IS NOT NULL)
      FROM trend_5m a JOIN trend_10m b USING(id_ticker,date,time)
      JOIN trend_15m c USING(id_ticker,date,time) JOIN trend_mean m USING(id_ticker,date,time)
      GROUP BY a.ticker,a.date'''
    agree_rows = labels.execute(agree_sql).fetchall()
    all_agree = [0] * 12
    root_day_agree = {}
    for row in agree_rows:
        ticker, day, *vals = row
        for i, v in enumerate(vals):
            all_agree[i] += int(v or 0)
        root = next((r for r in roots if ticker.startswith(r)), None)
        if root:
            k = (root, day)
            x = root_day_agree.setdefault(k, [0] * 12)
            for i, v in enumerate(vals):
                x[i] += int(v or 0)

    print('Checking source row count', flush=True)
    source_count = source.execute('SELECT COUNT(*) FROM price1').fetchone()[0]
    print('Writing report', flush=True)

    a.report.parent.mkdir(parents=True, exist_ok=True)
    a.session_csv.parent.mkdir(parents=True, exist_ok=True)
    fields = ['root','date','timeframe','tickers','rows','valid','nulls','up','down','coverage','changes','valid_transitions','changes_per_1000_transitions','runs','mean_run_candles','gap_events','missing_minutes','triple_valid','all_three_equal','mean_matches_majority','mean_majority_mismatch','pair_5m_10m_n','pair_5m_10m_agreement','pair_5m_15m_n','pair_5m_15m_agreement','pair_10m_15m_n','pair_10m_15m_agreement']
    with a.session_csv.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader()
        for tf, groups in by_tf.items():
            for (root, day), s in sorted(groups.items()):
                ag = root_day_agree.get((root, day), [0] * 12)
                _, n, valid, nulls, up, down, trans, changes, gaps, missing, runs, _ = s
                w.writerow(dict(root=root,date=day,timeframe=tf,tickers=s[0],rows=n,valid=valid,nulls=nulls,up=up,down=down,
                  coverage=f'{valid/n:.6f}' if n else '',changes=changes,valid_transitions=trans,
                  changes_per_1000_transitions=f'{1000*changes/trans:.3f}' if trans else '',runs=runs,
                  mean_run_candles=f'{valid/runs:.3f}' if runs else '',gap_events=gaps,missing_minutes=missing,
                  triple_valid=ag[1],all_three_equal=ag[2],mean_matches_majority=ag[3],mean_majority_mismatch=ag[4],
                  pair_5m_10m_n=ag[7],pair_5m_10m_agreement=f'{ag[6]/ag[7]:.6f}' if ag[7] else '',
                  pair_5m_15m_n=ag[9],pair_5m_15m_agreement=f'{ag[8]/ag[9]:.6f}' if ag[9] else '',
                  pair_10m_15m_n=ag[11],pair_10m_15m_agreement=f'{ag[10]/ag[11]:.6f}' if ag[11] else ''))

    report = [
      '# Auditoria de rótulos B4 (somente leitura)','',
      'Reproduzível por `scripts/audit_labels.py`; bancos SQLite abertos com `mode=ro`.','',
      '## Integridade e proveniência','',
      f'- B4 `{a.label_db}`: {a.label_db.stat().st_size} bytes; SHA-256 `{digest(a.label_db)}`; `quick_check=ok` verificado na Fase 0.',
      f'- Fonte `{a.source_db}`: {a.source_db.stat().st_size} bytes; SHA-256 `{digest(a.source_db)}`; confere com `label_run.source_sha256`: {digest(a.source_db)==meta["source_sha256"]}.',
      f'- Manifesto `{a.manifest}`: SHA-256 `{digest(a.manifest)}`; hash/tamanho do artefato conferem com o B4 local: {digest(a.label_db)==json_field(a.manifest,"artifact_sha256")}.',
      f'- Configuração de universo `{a.universe_config}`: SHA-256 `{digest(a.universe_config)}`; raízes futuras: {", ".join(roots)}.',
      f'- B4 `{meta["label_version"]}` gerado por `{meta["algorithm_id"]}`; período {meta["date_min"]}–{meta["date_max"]}; {meta["ticker_count"]} tickers e {meta["date_count"]} pregões.',
      f'- `price1` tem {source_count} linhas; `label_run.source_candle_rows`={meta["source_candle_rows"]}; os hashes da fonte são idênticos.',
      '', '## Cobertura e prevalência global','',
      '| Tabela | Linhas | Válidas | Nulas | Classe 0 | Classe 1 | Cobertura | Prevalência classe 1 |','|---|---:|---:|---:|---:|---:|---:|---:|']
    for tf in ('5m','10m','15m'):
        n, valid, down, up, nulls = labels.execute(f'SELECT COUNT(*),SUM(trend_label IS NOT NULL),SUM(trend_label=0),SUM(trend_label=1),SUM(trend_label IS NULL) FROM trend_{tf}').fetchone()
        report.append(f'| trend_{tf} | {n} | {valid} | {nulls} | {down} | {up} | {valid/n:.4%} | {up/valid:.4%} |')
    n, valid, down, up, nulls = labels.execute('SELECT COUNT(*),SUM(trend_label IS NOT NULL),SUM(trend_label=0),SUM(trend_label=1),SUM(trend_label IS NULL) FROM trend_mean').fetchone()
    report.append(f'| trend_mean | {n} | {valid} | {nulls} | {down} | {up} | {valid/n:.4%} | {up/valid:.4%} |')
    total, triple, equal, mean_ok, mean_bad, score_bad, a510, n510, a515, n515, a1015, n1015 = all_agree[0:12]
    report += ['', '## Concordância global','',f'- Chaves alinhadas nas quatro tabelas: {total}.','',
      '| Medida | Casos | Concordância/resultado |','|---|---:|---:|',
      f'| Três alvos válidos | {triple} | — |',f'| Três classes iguais | {triple} | {equal/triple:.4%} |',
      f'| `trend_mean` igual ao voto majoritário | {triple} | {mean_ok/triple:.4%}; divergências/nulos {mean_bad} |',
      f'| `mean_score` igual à média dos três rótulos | {triple} | divergências/nulos {score_bad} |',
      f'| 5m × 10m | {n510} | {a510/n510:.4%} |',f'| 5m × 15m | {n515} | {a515/n515:.4%} |',f'| 10m × 15m | {n1015} | {a1015/n1015:.4%} |',
      '', '## Universo de contratos futuros','',
      '| Raiz | Contrato | Pregões | Período | Candles | Cobertura 5m | Cobertura 10m | Cobertura 15m |',
      '|---|---|---:|---|---:|---:|---:|---:|']
    contract_names = sorted({ticker for entries in by_contract.values() for ticker in entries if any(ticker.startswith(r) for r in roots)})
    for ticker in contract_names:
        root = next(r for r in roots if ticker.startswith(r))
        vals = [by_contract[tf][ticker] for tf in ('5m','10m','15m')]
        c = vals[0]
        cov = [f'{x["valid"]/x["rows"]:.4%}' if x['rows'] else 'n/a' for x in vals]
        report.append(f'| {root} | {ticker} | {c["days"]} | {c["first"]}–{c["last"]} | {c["rows"]} | {cov[0]} | {cov[1]} | {cov[2]} |')
    report += ['', '## Cobertura e transições por raiz e escala','',
      '| Raiz | Escala | Pregões-raiz | Candles | Cobertura | Prev. classe 1 | Mudanças/1.000 transições | Duração média do segmento (candles) | Minutos ausentes |','|---|---|---:|---:|---:|---:|---:|---:|---:|']
    for tf, groups in by_tf.items():
        sums = defaultdict(lambda: [0] * 11)
        for (root, _day), s in groups.items():
            x = sums[root]
            for i, pos in enumerate((0,1,2,3,4,5,6,7,8,9)):
                x[i] += s[pos]
            x[10] += 1
        for root in roots:
            g = sums[root]
            tickers, n, valid, nulls, up, down, trans, changes, gaps, missing, days = g
            runs = sum(s[10] for (r,_),s in groups.items() if r==root)
            if n:
                coverage = f'{valid/n:.4%}' if n else 'n/a'
                prevalence = f'{up/valid:.4%}' if valid else 'n/a'
                change_rate = f'{1000*changes/trans:.3f}' if trans else 'n/a'
                duration = f'{valid/runs:.3f}' if runs else 'n/a'
                report.append(f'| {root} | {tf} | {days} | {n} | {coverage} | {prevalence} | {change_rate} | {duration} | {missing} |')
    report += ['', 'O CSV `label_audit_by_root_session.csv` contém as métricas por raiz, pregão e escala. Mudanças/segmentos usam pares de rótulos válidos em candles consecutivos separados por um minuto; lacunas interrompem segmentos.', '', '## Limites','',
      '- A classificação por raiz usa `future_roots` da configuração BovDB aprovada; contratos da mesma raiz não são aqui emendados/ajustados numa série contínua.',
      '- A chave primária garante unicidade dentro das tabelas, e hash/contagem confirmam a mesma fotografia de origem; não foi feito anti-join candle a candle entre bases por custo de leitura.',
      '- A auditoria descreve os alvos B0 e não seleciona indicadores nem treina modelos. A decisão sobre vencimentos/rolagem segue pendente da Fase 2.',
      '- Prevalência é ponderada por candle; para inferência, pregões/blocos continuam sendo as unidades de incerteza.','']
    a.report.write_text('\n'.join(report), encoding='utf-8')
    print(f'Wrote {a.report} and {a.session_csv}', flush=True)
    labels.close(); source.close()


def json_field(path, field):
    import json
    return json.loads(path.read_text(encoding='utf-8-sig'))[field]


if __name__ == '__main__':
    main()
