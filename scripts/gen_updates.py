#!/usr/bin/env python3
import subprocess, pathlib, datetime

out = pathlib.Path("docs/site-content/_fragments/latest-updates.md")
out.parent.mkdir(parents=True, exist_ok=True)

try:
    log = subprocess.check_output(
        ["git", "log", "-n", "5", "--pretty=format:- %ad — **%s**  \n  _by %an_",
         "--date=short"],
        text=True
    )
except Exception as e:
    log = f"- (no git log available)  \n  _{e}_"

content = f"""## 🗓️ Latest Updates

{log}

<sub>Generated on {datetime.date.today().isoformat()}</sub>
"""
out.write_text(content, encoding="utf-8")
print(f"Wrote {out}")
