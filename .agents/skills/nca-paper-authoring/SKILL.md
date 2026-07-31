---
name: nca-paper-authoring
description: Expert guidelines for authoring, structuring, formatting, and compiling papers for Neural Computing and Applications (NCA, Springer Nature).
---

# NCA Paper Authoring Skill

Use this skill when drafting, modifying, or reviewing LaTeX content for the **Neural Computing and Applications (NCA)** journal (Springer Nature, Journal ID 521, ISSN: 0941-0643).

## 1. Key Editorial Rules (NCA Journal)

- **Class & Style**: Always use `sn-jnl.cls` with `sn-mathphys-num`.
- **Double-Blind Peer Review**: The main manuscript (`main.tex` and files under `sections/`) MUST be completely anonymized.
- **Title Page**: Author metadata, ORCIDs, affiliations, and grant acknowledgments MUST reside in `titlepage.tex`.
- **Abstract & Keywords**: Abstract must be 150–250 words; 4–6 keywords.
- **Table Formatting**: Use `booktabs` (`\toprule`, `\midrule`, `\botrule`) and wrap tables in `\resizebox{\linewidth}{!}{...}` to prevent horizontal margin overflow.
- **Figures**: Resolution 1200 dpi for vector EPS, 300 dpi for TIFF/JPEG halftone.

## 2. Introduction Structure (CARS Model)

Follow the 5 rhetorical moves:
1. **Territory**: Establish high-frequency intraday market non-stationarity.
2. **Neural Role**: Present MLP universal approximation capabilities and hyperparameter complexity.
3. **Optimizer Isolation**: Transmit focus to metaheuristic algorithms (GA, PSO, DE, GWO, RS).
4. **Research Gap & Open Issues**: Detail Table 1 literature limitations and list open issues.
5. **6 Bulleted Contributions**: List 6 bold bullet points starting with active present-tense verbs.
