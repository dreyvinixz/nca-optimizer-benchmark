#!/usr/bin/env python3
"""Read-only liquidity summary for futures present in the BovDB one-minute table."""
import argparse
import os
import re
import sqlite3
from collections import defaultdict
from pathlib import Path
from statistics import median


def roots_from_yaml(path):
    lines = path.read_text(encoding='utf-8-sig').splitlines()
    start = next(i for i, line in enumerate(lines) if re.match(r'^\s{2}future_roots:\s*$', line))
    roots = []
    for line in lines[start + 1:]:
        if re.match(r'^\s{2}\S', line):
            break
        m = re.match(r'^\s{4,}-\s+([A-Z0-9]+)\s*$', line)
        if m:
            roots.append(m.group(1))
    return roots


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source-db', type=Path, default=Path(os.getenv('BOVDB_SOURCE_DB','data/bovdb-v3.1-internal.2.sqlite')))
    ap.add_argument('--labels-db', type=Path, default=Path(os.getenv('BOVDB_B4_DB','data/bovdb-labels-B4-v1.sqlite')))
    ext = Path('/mnt/c/mysystems/services/bovdb') if os.name != 'nt' else Path(r'C:\mysystems\services\bovdb')
    ap.add_argument('--universe-config', type=Path, default=Path(os.getenv('BOVDB_UNIVERSE_CONFIG',str(ext/'bovdb-pipeline/config/v3_1_universe.yaml'))))
    ap.add_argument('--report', type=Path, default=Path('reports/futures_liquidity.md'))
    a=ap.parse_args()
    approved=roots_from_yaml(a.universe_config)
    candidates=list(dict.fromkeys(approved+['WDO','WSP','ISP']))
    db=sqlite3.connect(a.source_db.resolve().as_uri()+'?mode=ro',uri=True)
    rows=db.execute("""SELECT t.ticker,p.date,SUM(COALESCE(p.amount_stock,0)),
      SUM(COALESCE(p.business,0)),SUM(COALESCE(p.volume,0)),COUNT(*)
      FROM price1 p JOIN ticker t USING(id_ticker) WHERE t.id_type=3
      GROUP BY t.ticker,p.date ORDER BY t.ticker,p.date""").fetchall()
    daily=defaultdict(lambda:defaultdict(lambda:[0,0,0,0]))
    symbols=defaultdict(set)
    for ticker,day,qty,biz,brl,rows_n in rows:
        root=next((r for r in candidates if ticker.startswith(r)),None)
        if root:
            x=daily[root][day]
            for i,v in enumerate((qty,biz,brl,rows_n)):
                x[i]+=v or 0
            symbols[root].add(ticker)
    absent_checks={}
    labels=sqlite3.connect(a.labels_db.resolve().as_uri()+'?mode=ro',uri=True)
    for root in ('WDO','WSP','ISP'):
        master_n=db.execute('SELECT COUNT(*) FROM ticker WHERE ticker LIKE ?', (root+'%',)).fetchone()[0]
        price_n=db.execute('SELECT COUNT(*) FROM price1 p JOIN ticker t USING(id_ticker) WHERE t.ticker LIKE ?', (root+'%',)).fetchone()[0]
        label_n={table:labels.execute(f'SELECT COUNT(*) FROM {table} WHERE ticker LIKE ?', (root+'%',)).fetchone()[0] for table in ('trend_5m','trend_10m','trend_15m')}
        absent_checks[root]={'ticker_master':master_n,'price1_rows':price_n,'b4_rows':label_n}
    a.report.parent.mkdir(parents=True,exist_ok=True)
    out=['# Liquidez dos futuros na base intradiária (somente leitura)','',
      'Fonte: `price1` do BovDB v3.1-internal.2; sessão por data, agregando contratos da mesma raiz. A métrica primária é `amount_stock` (quantidade negociada de contratos); `business` (negócios) é secundária. `volume` é financeiro em BRL e aparece como contexto, pois o notional/multiplicador varia por produto. Medianas são calculadas entre pregões com linhas presentes.','',
      f'- Janela da fonte: {db.execute("SELECT MIN(date),MAX(date) FROM price1").fetchone()[0]} a {db.execute("SELECT MIN(date),MAX(date) FROM price1").fetchone()[1]}.',
      f'- Raízes aprovadas na configuração atual: {", ".join(approved)}; `WDO`, `WSP` e `ISP` foram incluídos como candidatos explícitos à checagem.',
      '', '| Ordem por mediana | Raiz | Contratos presentes | Pregões observados | Mediana contratos/dia | Mediana negócios/dia | Mediana volume financeiro BRL/dia | Mediana minutos com negócio/dia |', '|---:|---|---|---:|---:|---:|---:|---:|']
    stats=[]
    for root in candidates:
        days=daily.get(root,{})
        if not days:
            stats.append((root,[],0,0,0,0,0))
            continue
        values=list(days.values())
        stats.append((root,sorted(symbols[root]),len(values),median(v[0] for v in values),median(v[1] for v in values),median(v[2] for v in values),median(v[3] for v in values)))
    ranked=sorted([s for s in stats if s[2]],key=lambda x:x[3],reverse=True)
    for i,(root,syms,days,qty,biz,brl,minutes) in enumerate(ranked,1):
        out.append(f'| {i} | {root} | {", ".join(syms)} | {days} | {qty:,.0f} | {biz:,.0f} | {brl:,.2f} | {minutes:,.0f} |')
    for root in ('WDO','WSP','ISP'):
        if not daily.get(root):
            out.append(f'| — | {root} | — | 0 | n/a | n/a | n/a | 0 |')
    out += ['', '## Verificação de disponibilidade dos candidatos', '', '| Raiz | Registros no cadastro de tickers | Linhas price1 | Linhas B4 5m | Linhas B4 10m | Linhas B4 15m |', '|---|---:|---:|---:|---:|---:|---:|']
    for root, info in absent_checks.items():
        out.append(f"| {root} | {info['ticker_master']:,} | {info['price1_rows']:,} | {info['b4_rows']['trend_5m']:,} | {info['b4_rows']['trend_10m']:,} | {info['b4_rows']['trend_15m']:,} |")
    out += ['', '## Leitura e limite','',
      '- Na amostra atualmente disponível, WIN e IND lideram claramente em quantidade de contratos e negócios. WDO, WSP e ISP sem candles/labels locais não podem ser ranqueados.',
      '- Os registros são a cobertura local da fonte BovDB, não uma auditoria independente de completude de mercado. Ausência local não significa que o produto não foi negociado no período.',
      '- A seleção do universo deve usar a liquidez pré-treino; a auditoria de rótulos B4 já realizada continua válida para as linhas existentes. Reexecutá-la só será necessário para símbolos novos se a fonte for ampliada.',
      '- As somas por raiz agregam contratos sobrepostos no mesmo dia; as janelas de features ainda devem manter a identidade do contrato e não atravessar rolagens.','']
    a.report.write_text('\n'.join(out),encoding='utf-8')
    print(f'Wrote {a.report}')
    labels.close()
    db.close()

if __name__=='__main__':
    main()
