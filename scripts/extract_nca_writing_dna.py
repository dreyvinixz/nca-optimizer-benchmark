import re
import sys
from pathlib import Path
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

md_dir = Path("article/references/md_references")
md_files = list(md_dir.rglob("*.md"))

print(f"=== ANALYZING {len(md_files)} MARKDOWN PAPERS FOR NCA WRITING DNA ===")

# Metrics collectors
intro_paras = []
intro_words_per_para = []
intro_words_per_sentence = []

relwork_paras = []
methods_paras = []
results_paras = []
disc_paras = []
concl_paras = []

passive_counts = Counter()
active_counts = Counter()

equation_intros = Counter()
table_intros = Counter()
figure_intros = Counter()
gap_connectives = Counter()
transition_words = Counter()

# Common transition words to search
transitions_to_check = [
    "however", "nevertheless", "furthermore", "moreover", "consequently",
    "specifically", "in contrast", "to address", "accordingly", "subsequently",
    "on the other hand", "crucially", "notably", "therefore", "thus"
]

for mf in md_files:
    text = mf.read_text(encoding="utf-8", errors="ignore")
    
    # Split by headers
    sections = re.split(r'\n(?=#|\n##|\n###)', text)
    
    for sec in sections:
        sec_lower = sec.lower()
        lines = [l.strip() for l in sec.splitlines() if l.strip() and not l.strip().startswith('#')]
        paras = [p for p in sec.split('\n\n') if len(p.strip()) > 50 and not p.strip().startswith('#')]
        
        # Check transition words
        for tw in transitions_to_check:
            cnt = len(re.findall(r'\b' + tw + r'\b', sec_lower))
            if cnt > 0:
                transition_words[tw] += cnt
        
        # Section classification
        if any(h in sec_lower[:100] for h in ["introduction", "1 introduction", "1. introduction"]):
            intro_paras.append(len(paras))
            for p in paras:
                words = p.split()
                intro_words_per_para.append(len(words))
                sentences = re.split(r'[\.\?!]\s+', p)
                for s in sentences:
                    if len(s.split()) > 3:
                        intro_words_per_sentence.append(len(s.split()))
        
        elif any(h in sec_lower[:100] for h in ["related work", "literature review", "2 related"]):
            relwork_paras.append(len(paras))
        elif any(h in sec_lower[:100] for h in ["methodology", "method", "proposed framework", "3 methodology", "4 methodology"]):
            methods_paras.append(len(paras))
        elif any(h in sec_lower[:100] for h in ["results", "experimental results", "5 results", "4 results"]):
            results_paras.append(len(paras))
        elif any(h in sec_lower[:100] for h in ["discussion", "6 discussion"]):
            disc_paras.append(len(paras))
        elif any(h in sec_lower[:100] for h in ["conclusion", "7 conclusion"]):
            concl_paras.append(len(paras))

        # Phrasing patterns
        eq_matches = re.findall(r'(\b(?:equation|eq\.|given by|defined as|expressed as)\b[^\.\?!]+)', sec_lower)
        for em in eq_matches[:2]:
            equation_intros[em[:50].strip()] += 1

        tbl_matches = re.findall(r'(\b(?:table \d|table \ref|summarizes|presents|depicts|reports)\b[^\.\?!]+)', sec_lower)
        for tm in tbl_matches[:2]:
            table_intros[tm[:50].strip()] += 1

print("\n--- STATISTICAL DNA EXTRACTED ---")
if intro_paras:
    print(f"Avg Intro Paragraphs per Paper: {sum(intro_paras)/len(intro_paras):.1f}")
if intro_words_per_para:
    print(f"Avg Words per Intro Paragraph: {sum(intro_words_per_para)/len(intro_words_per_para):.1f}")
if intro_words_per_sentence:
    print(f"Avg Words per Sentence in Intro: {sum(intro_words_per_sentence)/len(intro_words_per_sentence):.1f}")

print("\nMost Frequent Transition Words across NCA Corpus:")
for tw, cnt in transition_words.most_common(10):
    print(f"  • {tw}: {cnt} occurrences")
