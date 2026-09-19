import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

URL = "https://www.mucabrasil.com.br/?go=guild&n=EMPIRE4"
OUT = Path("data/resets.json")

req = Request(URL, headers={
    "User-Agent": "Mozilla/5.0 (compatible; EMPIRE4-Reset-Monitor/1.0)"
})

with urlopen(req, timeout=30) as response:
    html = response.read().decode("utf-8", errors="ignore")

# Remove tags so the parser is resilient to small HTML layout changes.
text = re.sub(r"<[^>]+>", " ", html)
text = re.sub(r"\s+", " ", text)

# The current MUCABRASIL page exposes: Resets: 13040
match = re.search(r"Resets\s*:\s*([0-9][0-9.,]*)", text, re.I)
members = re.search(r"Membros\s*:\s*([0-9][0-9.,]*)", text, re.I)

if not match:
    raise RuntimeError("Não foi possível localizar o campo Resets na página do MUCABRASIL.")

def number(value):
    return int(re.sub(r"\D", "", value))

data = {
    "guild": "EMPIRE4",
    "resets": number(match.group(1)),
    "members": number(members.group(1)) if members else None,
    "updated_at": datetime.now(timezone.utc).isoformat(),
    "source": URL
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(data, ensure_ascii=False, indent=2))
