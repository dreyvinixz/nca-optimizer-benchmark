# Phase 7 decision: no optional extension

**Decision date:** 2026-10-26

**Status:** not executed; extension phase formally closed for this project version.

The Phase 7 gate required a useful signal in Phase 5 before starting an extension. Development-fold paired inference found near-zero independent-minus-shared MCC differences at all three scales, with all Holm-adjusted Wilcoxon p-values equal to 1.00 and all five-session bootstrap intervals covering zero. The final held-out test retained that result: all three paired MLP MCC-difference intervals include zero.

The soft-score MLP does improve on its training-mean constant, but this is part of the planned Phase 5 comparison and predicts a deterministic fraction of the same B0 votes. It does not provide independent validation or motivate a separate representation-learning, pretraining, or regime-adaptation hypothesis.

Accordingly, no self-supervised pretraining, frozen temporal encoder, regime adaptation, or additional ablation was run. The existing core model comparisons remain unchanged. Reconsider an extension only under a new protocol and independent rationale; do not use these test results to select new model settings for this study.
