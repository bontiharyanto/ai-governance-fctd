#!/usr/bin/env python3
import os, shutil, re, sys

ROOT = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
DOCS_DIR = os.path.join(ROOT, "docs", "site-content")
SRC_REPORTS = os.path.join(ROOT, "reports")
DST_REPORTS = os.path.join(DOCS_DIR, "research", "reports")
RESULTS_MD = os.path.join(DOCS_DIR, "research", "results.md")
GEN_DIR = os.path.join(DOCS_DIR, "research", "_generated")

def ensure_dirs():
    os.makedirs(DST_REPORTS, exist_ok=True)
    os.makedirs(GEN_DIR, exist_ok=True)

def copy_pngs():
    if not os.path.isdir(SRC_REPORTS):
        print(f"[skip] source reports dir not found: {SRC_REPORTS}")
        return []
    copied = []
    for fn in os.listdir(SRC_REPORTS):
        if fn.lower().endswith(".png"):
            src = os.path.join(SRC_REPORTS, fn)
            dst = os.path.join(DST_REPORTS, fn)
            shutil.copy2(src, dst)
            copied.append(fn)
    print(f"[ok] copied PNGs: {copied}")
    return copied

def copy_jsons():
    # salin JSON hasil analisis ke _generated agar bisa di-include kalau perlu
    moved = []
    for fn in ["results_survey.json", "reliability.json", "stats_tests.json", "power.json"]:
        src = os.path.join(ROOT, fn)
        if os.path.isfile(src):
            dst = os.path.join(GEN_DIR, fn)
            shutil.copy2(src, dst)
            moved.append(fn)
    print(f"[ok] copied JSONs to _generated/: {moved}")
    return moved

def patch_results_md():
    if not os.path.isfile(RESULTS_MD):
        print(f"[warn] results.md not found: {RESULTS_MD}")
        return False
    with open(RESULTS_MD, "r", encoding="utf-8") as f:
        s = f.read()

    # Normalisasi semua kemungkinan path lama → "reports/<file>.png"
    # contoh pola yang disasar:
    #  ../../reports/file.png, ../../../reports/file.png, /reports/file.png
    s2 = re.sub(r'\((?:\.\./)+reports/([^)\s]+)\)', r'(reports/\1)', s)
    s2 = re.sub(r'\(/?reports/([^)\s]+)\)', r'(reports/\1)', s2)

    if s2 != s:
        with open(RESULTS_MD, "w", encoding="utf-8") as f:
            f.write(s2)
        print("[ok] results.md links rewritten to 'reports/...'.")
        return True
    else:
        print("[ok] results.md already uses 'reports/...'.")
        return False

def main():
    ensure_dirs()
    copy_pngs()
    copy_jsons()
    patch_results_md()
    print("[done] sync complete.")

if __name__ == "__main__":
    sys.exit(main())
