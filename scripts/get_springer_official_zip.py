import urllib.request
import re
import os

url = "https://www.springernature.com/gp/authors/campaigns/latex-author-support/see-where-our-services-will-take-you/18782940"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})

print(f"Fetching: {url}")
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode("utf-8", errors="ignore")

print(f"HTML size: {len(html)} bytes")

# Find all links containing .zip or download
matches = re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html, re.DOTALL | re.IGNORECASE)
print(f"Found {len(matches)} links total.")

zip_links = []
for href, text in matches:
    clean_text = re.sub(r'<[^>]+>', '', text).strip()
    if ".zip" in href.lower() or "download" in clean_text.lower() or "template" in clean_text.lower() or "latex" in clean_text.lower():
        full_url = href
        if href.startswith("//"):
            full_url = "https:" + href
        elif href.startswith("/"):
            full_url = "https://www.springernature.com" + href
        print(f"  Match: [{clean_text}] -> {full_url}")
        if ".zip" in full_url.lower() or "download" in full_url.lower():
            zip_links.append((clean_text, full_url))

# Also search for static zip assets in the HTML text
all_zips = re.findall(r'https?://[^\s"\'<>]+\.zip', html, re.IGNORECASE)
for z in all_zips:
    print(f"  Static ZIP asset found: {z}")
    zip_links.append(("Static ZIP", z))

out_dir = os.path.abspath("article/templates")
os.makedirs(out_dir, exist_ok=True)

if zip_links:
    for text, z_url in zip_links:
        print(f"\nAttempting download: {z_url}")
        target_path = os.path.join(out_dir, "springer_nature_official_latex_template.zip")
        try:
            req_dl = urllib.request.Request(z_url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
            with urllib.request.urlopen(req_dl) as dl_resp, open(target_path, "wb") as f:
                f.write(dl_resp.read())
            print(f"SUCCESS: Saved official template to {target_path} ({os.path.getsize(target_path)} bytes)")
            break
        except Exception as e:
            print(f"Failed {z_url}: {e}")
else:
    print("No ZIP links found on the page.")
