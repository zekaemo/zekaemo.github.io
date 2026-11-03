from pathlib import Path
import re

root = Path(__file__).resolve().parents[1] / "public"
missing = []
for page in root.rglob("*.html"):
    for url in re.findall(r'(?:src|href)="(/[^"#]*)', page.read_text()):
        target = root / url.split("?")[0].lstrip("/")
        if not target.exists():
            missing.append(f"{page.relative_to(root)}: {url}")
if missing:
    raise SystemExit("Missing targets:\n" + "\n".join(missing))
print("All HTML asset and route targets exist.")
