import re
import os
from pathlib import Path

step_62_file = Path(os.path.expanduser(r"~\.gemini\antigravity-ide\brain\162d26c4-b837-4bb4-bf80-256d2bc8ab75\.system_generated\steps\62\content.md"))

print(f"Reading from: {step_62_file}")
html = step_62_file.read_text(encoding="utf-8", errors="ignore")
print(f"Total HTML length: {len(html)} bytes")

# Remove scripts, styles, svg
html_clean = re.sub(r'<script.*?>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
html_clean = re.sub(r'<style.*?>.*?</style>', '', html_clean, flags=re.DOTALL | re.IGNORECASE)
html_clean = re.sub(r'<svg.*?>.*?</svg>', '', html_clean, flags=re.DOTALL | re.IGNORECASE)

# Extract headings, paragraphs, lists, sections
blocks = re.findall(r'<(h[1-6]|p|li|span|dt|dd)[^>]*>(.*?)</\1>', html_clean, re.DOTALL | re.IGNORECASE)

lines = []
lines.append("# Neural Computing and Applications — Submission Guidelines")
lines.append("**Source URL**: https://link.springer.com/journal/521/submission-guidelines")
lines.append("**Journal**: Neural Computing and Applications (Springer Nature, ISSN: 0941-0643)")
lines.append("---\n")

seen = set()
for tag, content in blocks:
    text = re.sub(r'<[^>]+>', ' ', content)
    text = re.sub(r'\s+', ' ', text).strip()
    if not text or len(text) < 5 or text in seen:
        continue
    
    # Filter website navigation UI text
    if any(skip in text.lower() for skip in ['javascript', 'cookie consent', 'skip to main content', 'springer link logo', 'search article', 'log in button']):
        continue

    seen.add(text)
    
    if tag.startswith('h'):
        level = int(tag[1])
        lines.append(f"\n{'#' * max(2, level)} {text}\n")
    elif tag == 'li':
        lines.append(f"- {text}")
    elif tag in ['dt', 'dd']:
        lines.append(f"**{text}**" if tag == 'dt' else f"{text}\n")
    else:
        lines.append(f"\n{text}\n")

out_file = Path(__file__).resolve().parent.parent / "article" / "references" / "nca_submission_guidelines.md"
out_file.parent.mkdir(parents=True, exist_ok=True)

out_file.write_text("\n".join(lines), encoding="utf-8")
print(f"SUCCESS: Saved guidelines to {out_file} ({out_file.stat().st_size} bytes)")
