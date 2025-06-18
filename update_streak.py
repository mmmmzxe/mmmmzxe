import requests

USERNAME = "mmmmzxe"  # ← غيّريه لو اسمك مختلف

url = f"https://streak-stats.demolab.com?user={USERNAME}&hide_border=true"
response = requests.get(url)

if "Current Streak" in response.text:
    import re
    match = re.search(r'Current Streak.*?(\d+)\s+days', response.text)
    if match:
        days = match.group(1)
    else:
        days = "0"
else:
    days = "0"

badge = f"![Streak](https://img.shields.io/badge/Streak-🔥%20{days}%20days-orange?style=for-the-badge)\n"

with open("streak-badge.md", "w", encoding="utf-8") as f:
    f.write(badge)

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

new_content = re.sub(
    r"<!-- BEGIN_STREAK -->(.*?)<!-- END_STREAK -->",
    f"<!-- BEGIN_STREAK -->\n{badge}<!-- END_STREAK -->",
    content,
    flags=re.DOTALL
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)

