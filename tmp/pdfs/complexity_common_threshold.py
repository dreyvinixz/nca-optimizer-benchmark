from pathlib import Path
import csv
import pandas as pd
ROOT=Path('outputs')
def read_run(f):
    with f.open('r',newline='',encoding='utf-8-sig') as s: rows=list(csv.reader(s))
    return pd.DataFrame([r[:len(rows[0])] for r in rows[1:]],columns=rows[0])
EXPS={'MCC/F1 holdout':('article_official',1),'weighted-accuracy holdout':('article_official_accuracy_holdout',1),'weighted-accuracy temporal CV':('article_official_accuracy',3)}
for exp,(folder,folds) in EXPS.items():
    m=ROOT/folder/'metrics'
    conv=pd.concat([pd.read_csv(f) for f in (m/'convergence').glob('*_convergence.csv')],ignore_index=True)
    runs=pd.concat([read_run(f) for f in m.glob('*_runs.csv')],ignore_index=True)
    conv=conv[conv.evaluation_id.le(1000)].copy()
    runs=runs[runs.candidate_id.astype(int).le(1000)].copy()
    print('\n###',exp)
    out=[]
    for model,g in conv.groupby('model_type'):
        first=g[g.evaluation_id.eq(10)].groupby(['optimizer','seed']).best_fitness_so_far.first()
        base=first.mean()
        finals=g[g.evaluation_id.eq(1000)].groupby(['optimizer','seed']).best_fitness_so_far.last()
        end_by_opt=finals.groupby('optimizer').mean()
        bestopt=end_by_opt.idxmax(); target=base+.95*(end_by_opt.max()-base)
        print(model,'base',round(base,5),'best optimizer mean',bestopt,round(end_by_opt.max(),5),'common95 target',round(target,5))
        for opt in sorted(g.optimizer.unique()):
            vals=[]
            for seed,sg in g[g.optimizer.eq(opt)].groupby('seed'):
                hits=sg[sg.best_fitness_so_far.ge(target)]
                if hits.empty: vals.append((seed,None,None)); continue
                ev=int(hits.evaluation_id.iloc[0])
                rr=runs[(runs.model_type.eq(model))&(runs.optimizer.eq(opt))&(runs.seed.eq(seed))&(runs.candidate_id.astype(int).le(ev))].sort_values('candidate_id')
                fit=int((~rr.cache_hit.astype(str).str.lower().eq('true')).sum()*folds)
                vals.append((seed,ev,fit))
            attained=[x for x in vals if x[1] is not None]
            fitmed=round(pd.Series([x[2] for x in attained]).median(),1) if attained else None
            out.append((opt,fitmed,len(attained),sum(x[1] is None for x in vals)))
    df=pd.DataFrame(out,columns=['optimizer','median_fits_when_reached','seeds_reached','seeds_unreached'])
    print(df.to_string(index=False))
