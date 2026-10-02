from pathlib import Path
import pandas as pd
root=Path('outputs')
experiments={'MCC/F1 holdout':'article_official','weighted-accuracy holdout':'article_official_accuracy_holdout','weighted-accuracy temporal CV':'article_official_accuracy'}
steps=[100,250,500,750,1000]
for label,folder in experiments.items():
    frames=[]
    for f in (root/folder/'metrics'/'convergence').glob('*_convergence.csv'):
        d=pd.read_csv(f)
        d=d[d['evaluation_id'].isin(steps)].copy()
        frames.append(d)
    all=pd.concat(frames,ignore_index=True)
    p=all.pivot_table(index=['model_type','evaluation_id'],columns='optimizer',values='best_fitness_so_far',aggfunc='mean')
    print('\n',label)
    for model in ['rf','svm','mlp','cnn']:
        print(model)
        for step in steps:
            r=p.loc[(model,step)]
            rs=r.get('random_search')
            best_other=r.drop(labels=['random_search']).max()
            worst=r.drop(labels=['random_search']).min()
            print(step, 'RS',round(rs,4),'best_other',round(best_other,4),'worst_other',round(worst,4),'RSbelowall',bool(rs<worst))
