import requests
import re

urls = [
    'https://www.springernature.com/gp/authors/campaigns/latex-author-support',
    'https://www.springer.com/gp/authors-editors/journal-author/journal-author-help-systems/latex-settup/3382',
    'https://www.springernature.com/gp/authors/publish-a-book/manuscript-guidelines'
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for url in urls:
    try:
        res = requests.get(url, headers=headers, timeout=10)
        print('Checking:', url, res.status_code)
        links = re.findall(r'href=["\']([^"\']+)["\']', res.text, re.I)
        for link in links:
            if 'zip' in link.lower() or 'latex' in link.lower() or 'template' in link.lower():
                if link.startswith('//'):
                    link = 'https:' + link
                elif link.startswith('/'):
                    link = 'https://www.springernature.com' + link
                print('  Found match:', link)
    except Exception as e:
        print('Error:', e)
