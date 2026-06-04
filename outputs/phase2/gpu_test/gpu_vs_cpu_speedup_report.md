# GPU vs CPU Speedup Report

- Matched evaluations: 100
- CPU average wall time/eval: 5.0452s
- GPU average wall time/eval: 0.1143s
- Observed speedup: 44.13x
- Projected CPU time for 25,000 evals: 35.04 hours
- Projected GPU time for 25,000 evals: 0.79 hours

## Summary Table

```
         Backend  Evaluations  Avg wall/eval (s)  Min wall/eval (s)  Max wall/eval (s)  Total wall time (s)  Best fitness  Avg fitness  Best MCC  Best F1  Avg CUDA kernel/eval (s)
CPU (tensorflow)          100           5.045174           2.414013           8.398101           504.517372      0.426986     0.410839  0.272625 0.662002                       NaN
      GPU (cuda)          100           0.114318           0.094697           0.187081            11.431771      0.426011     0.407620  0.272600 0.662203                  0.101742
```
