# Feature and label provenance audit

Audit date: 2026-10-02

This note records what the files currently in the repository establish about the
seven-feature representation and the pivot-label generation pipeline. It
distinguishes archived evidence from details that still require the original
label-generation project on the other SSD.

## Information Gain features

### Current benchmark mask

`outputs/professor_presentation/tables/infogain7_features.csv` records the
following ordered mask. The indices agree with
`config/experiment_config.yaml` (`selected_feature_set: InfoGain_7`):

| Index | Feature |
|---:|---|
| 30 | `EMA_5-3` |
| 52 | `EMA_5-3_normalized` |
| 31 | `EMA_7-3` |
| 53 | `EMA_7-3_normalized` |
| 42 | `SMA_9_normalized` |
| 33 | `EMA_9-3` |
| 41 | `EMA_7_normalized` |

This is direct evidence of the mask used by the present benchmark. The CSV
contains feature indices and names only; it does not record the source dataset,
the dates used to compute Information Gain, the selector settings, scores, or
the selection run's code/version.

### Feature ranking recorded in `cópia_de_tradingdata_categorico.py`

This second Colab export reads `/content/drive/MyDrive/merged_output.csv`,
defines the same Jan 1--Mar 30, 2024 training interval and Apr 1--Jun 30 test
interval, and hard-codes a complete 66-index `InfoGain` ranking. Its first
seven indices are `30, 52, 31, 53, 42, 33, 41`; mapping these indices through
the `X_train` column order in the file yields exactly the seven names listed
above. The script explicitly sets `best_selections_filtered['InfoGain']` to
the first seven, prints those names, and subsequently evaluates the fixed set.
Thus this file connects the current seven-feature mask to an explicit ordered
InfoGain ranking and shows the downstream experiment separating train and
test by date before fitting/evaluation.

The ranking itself is a hard-coded list in this file: the code does not
calculate or save the Information Gain scores that produced it. The researcher
has now confirmed that the WEKA ranking was calculated using only the
chronological training subset for January--March 2024, separated by the number
of rows/candles in that period, with the April--June test subset excluded.
Accordingly, the feature-selection leakage concern is resolved by the
researcher's direct account; the precise WEKA run remains unavailable for
independent software-level reproduction. The Python file also shows the
subsequent date split and use of the fixed seven-feature set. Its 9-fold
`cross_val_score` evaluation reports prefix performance, while the later
final-model/test section uses the explicitly fixed seven features.

### Earlier five-feature analysis

`cópia_de_tradingdata_categorico (1).py` is a separate feature-selection
analysis. It reads `/content/drive/MyDrive/merged_output_new.csv` and defines a
chronological training interval from 2024-01-01 through 2024-03-30 and a test
interval from 2024-04-01 through 2024-06-30. Its Information Gain selector
wraps `sklearn.feature_selection.mutual_info_classif` with `random_state=42`.
The reference ranking is fitted on the training interval. For incremental
subset evaluation, it uses 9-fold shuffled `StratifiedKFold` with
`random_state=42`, refits the selector within each fold's training portion,
then evaluates a 100-tree Random Forest (`random_state=42`) on that fold's
validation portion. The script sets `DECLINE_K['Information Gain'] = 5` and
uses the first five entries of the reference ranking. Thus, this file documents
an earlier five-feature procedure, not the present seven-feature mask.

The Python file computes and prints the ranked feature names and scores at
runtime; it does not hard-code that ranking. The corresponding
`merged_output_new.csv` and captured notebook output are not currently archived
in this repository, so the five names and their scores cannot be recovered from
this source file alone. The file does not establish the provenance of the
current seven-feature mask.

## Confirmed source of the benchmark labels

The original project databases were found at `D:\database`:
`Database_define.db` and `rotulos_price5.db`. I reproduced the routines in
`D:\bovdb\code\examples\candle_logic.py` and
`D:\bovdb\code\examples\rotulos_dabase_create.py` in memory, reading the
databases in read-only mode and making no database changes. The reproduction
matched all four stored label fields (`downtrend`, `uptrend`, `top`, `bottom`)
for every stored label row: **23,181/23,181 exact matches** across ticker IDs
2952, 2963, 2978, 3193, 3276, and 58413. Some source price rows are absent from
the label database; there were no label-database rows absent from the source
price data.

The article's `data/raw/merged_output.csv` contains 15,057 rows. Its `trend`
label equals the next retained `uptrend`/`downtrend` record for the same ticker
in **15,053/15,053** rows with a successor. This includes all 196 last-of-day
rows: each is aligned to the next retained observation for that contract,
usually in the following session. Four rows are the final retained observation
for their ticker; they have no successor and retain the current source label.
Thus, the earlier count of 196 “unverified” rows was caused by restricting the
comparison to the same day. It does not indicate 196 missing or mismatched
labels. The exact source-generation routine is recovered and the stored labels
are exactly reproducible from the archived database.

The recovered routine uses **60-minute (hourly) pivots**, not 15-minute
pivots. The current Methods, Discussion, and Conclusion text has been corrected
to say hourly. This is the routine that generated the label database matching
the benchmark CSV; the prior claim of 15-minute label generation was incorrect
for these archived labels.

## Alternate B3 pivot-label heuristic

`generate_chart_b3_regime.py` is a later B3 regime-analysis implementation,
not the source of the benchmark labels. Its input routine loads one-minute
bars, and its runner evaluates 15-, 10-, and 5-minute macro timeframes. It is
useful as a later related heuristic, but must not be cited as the generator of
the benchmark's labels.

The shared B0 pivot heuristic in `detectar_topos_fundos` does the following:

1. Resamples the supplied lower-timeframe candles into macro candles, using
   first open, last close, maximum high, minimum low, and summed volume and
   business count.
2. Groups consecutive bullish macro candles (`close > open`) and consecutive
   non-bullish macro candles (`close <= open`). For an up-run, it selects the
   macro candle with the highest close; for a down-run, the one with the lowest
   close.
3. Searches the corresponding lower-timeframe interval for the maximum or
   minimum **close**, respectively, and records that lower-timeframe timestamp
   as the pivot. The stored extreme is that candle's high for a top or low for
   a valley.
4. Checks the immediately following macro interval and moves the candidate
   pivot forward if that interval contains a more extreme close.
5. Sorts candidates by time and enforces strict top/valley alternation,
   retaining the more extreme of consecutive candidates of the same type.

`pivots_to_binary_trend_labels` labels the interval `(VALLEY, TOP]` as
uptrend and `(TOP, VALLEY]` as downtrend; the prefix through the first pivot
is labeled according to the first pivot type, and rows after the last pivot
remain unlabeled. The runner applies subsequent B1 structural and B2
significance filters before producing its binary B2 labels; its B3 step adds
sideways regimes for a separate three-class output. These later filters and
the current B3 settings must not be silently attributed to the historical
binary-label run.

This is a retrospective turning-point labeling rule: a pivot's location and
the segment endpoint depend on later candles (including the following macro
interval and, in B1/B2, later pivots/structure). It is appropriate to describe
the target as a pivot-defined regime label, but it does not by itself establish
when each label became available in the original production pipeline. The
The one-row shift aligns the five-minute feature row with the next retained
regime-label row for that ticker; it does not make the underlying retrospective
pivot label causal. For the last row of a session, that next row can occur in
the following session. Four final per-ticker rows have no forward row and are
retained with their contemporaneous label. Split-boundary/purge implications
therefore remain relevant.

## Archived implementation details on `D:\bovdb`

The repository at `D:\bovdb` contains the recovered historical label routine
in `code/examples/candle_logic.py` and its database-writing pipeline in
`code/examples/rotulos_dabase_create.py`. It calls
`DataProcessor.detectar_topos_fundos_60_min()`: this version uses **60-minute**
macro bars, not 15-minute bars. It resamples five-minute `price5` data into
60-minute OHLCV bars, groups consecutive bullish or bearish macro bars, finds
the highest/lowest close within each run, and refines the pivot to the
corresponding extreme five-minute close. It then checks the immediately
following 60-minute interval and moves the pivot if that interval contains a
more extreme close.

The labeling script flags the pivot row, carries the opposite directional
state forward after each pivot, resets the state on a date change, and
retroactively assigns the initial portion of the loaded series according to
its first top or bottom. It writes `downtrend`, `uptrend`, `top`, and `bottom`
columns to `Rotule_price5`. The source generator itself has no explicit
`shift(-1)` operation; the forward one-row alignment is applied downstream and
confirmed by comparing the modeling CSV to the saved database labels. The
referenced database files are available at `D:\database`, and the exact
reproduction results are recorded above.

## Claims safe to make now

- The present benchmark uses the seven-feature mask listed above.
- A separate earlier script describes a train-only Information Gain ranking
  and 9-fold incremental evaluation that selected a five-feature subset.
- The recovered 60-minute routine is the exact generator of the archived
  `Rotule_price5` labels and reproduces every stored row; the article dataset's
  one-row forward alignment is confirmed for every compared nonterminal row.
- `generate_chart_b3_regime.py` is a separate, later implementation and did
  not generate the benchmark labels.
- The seven-feature selection is confirmed by the researcher as train-only
  (January--March 2024); its original WEKA run/settings are not archived.
- The recovered label-generation code itself has no explicit `shift(-1)`;
  the one-row forward alignment is applied downstream and confirmed by direct
  comparison of the saved benchmark CSV with the archived label database.

## Boundary audit for the manuscript split

The 15,057-row dataset is split at observation indices 9,034 and 12,045.
Because the saved target at row `t` is the raw regime label at the next retained
row for the same ticker, one training target has a validation-period successor
and two validation targets have test-period successors. These three rows were
retained in the reported experiments. They are direct one-row target crossings,
distinct from the broader retrospective nature of hourly pivot labels.

The historical label routine was rerun in memory on source-price histories
truncated at the training and validation cutoffs. Among the other 9,032
training and 3,008 validation target rows checked, no saved label changed.
This rules out revisions for those checked rows under that cutoff-only replay,
but does not cure the direct crossings or establish causal availability of
retrospective pivots. The temporal-CV implementation also does not purge the
last training row of each fold, whose next-row target comes from the first
validation row of that fold.

Before submission, the direct crossings and four per-ticker terminal rows
should be purged or otherwise handled with a target-aware split; model
selection and reported test metrics should then be regenerated. The manuscript
now states that these rows were retained and qualifies the evidence. A clean
compile does not substitute for this purged rerun.

## Fitness protocol and RQ2 audit

The implementation in `src/objective.py` matches the manuscript's two holdout
objectives: Protocol A is `0.60*MCC_val + 0.40*F1_val`; Protocol B is
`0.40*Acc_train + 0.60*Acc_val`. Because Protocol B includes training accuracy
and uses another metric, their comparison is between complete selection
protocols, not an isolated test of metric choice. The three-fold temporal-CV
objective is the mean of `0.40*Acc_train_fold + 0.60*Acc_val_fold`; its fold
boundary is not purged for the one-row target shift.

The current RQ2 asks how backbones and selection protocols perform on a common
subsequent chronological test interval under temporal model selection. It does
not ask for a randomized-CV-versus-temporal-split comparison, so the earlier
review's criticism described obsolete wording. RQ2 is answered descriptively
by the two holdout experiments and the separately reported weighted-accuracy
temporal-CV experiment, subject to the boundary qualification above.
`config/protocol_experiments.yaml` was corrected to mark accuracy holdout as
run and to name accuracy CV as Experiment 3, consistent with its output
directory and the manuscript.
