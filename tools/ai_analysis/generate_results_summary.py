#!/usr/bin/env python3
import argparse, json, os

def load_json(path):
    try:
        with open(path,"r") as f: return json.load(f)
    except Exception:
        return {}

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Generate Markdown summary from results JSONs")
    ap.add_argument("--regress", default="results_survey.json")
    ap.add_argument("--reliability", default="reliability.json")
    ap.add_argument("--stats", default="stats_tests.json")
    ap.add_argument("--power", default="power.json")
    ap.add_argument("--out", default="docs/site-content/research/_generated/results_summary.md")
    args = ap.parse_args()

    reg = load_json(args.regress)
    rel = load_json(args.reliability)
    st  = load_json(args.stats)
    pw  = load_json(args.power)

    # ambil R2
    r2 = None
    if "regression" in reg:
        r2 = reg["regression"].get("r2") or reg["regression"].get("r2_score")
    # ambil alpha
    alpha = rel.get("alpha")
    items = rel.get("items", [])
    # stats test ringkas
    stats_line = "–"
    if st.get("type") == "anova":
        stats_line = f"ANOVA: F={st.get('F',0):.3f}, p={st.get('p',0):.3g}, groups={st.get('n_groups',0)}"
    elif st.get("type") == "ttest":
        stats_line = f"t-test: t={st.get('t',0):.3f}, p={st.get('p',0):.3g}, groups={st.get('n_groups',0)}"
    # power
    power_line = "–"
    if pw:
        eff = pw.get("effect_size")
        need = pw.get("min_total_samples")
        if eff and need:
            power_line = f"Effect size (d)={eff}, min total N≈{need:.1f}"

    md = []
    md.append("# 🔎 Hasil Ringkas Analisis\n")
    if r2 is not None:
        md.append(f"- **Goodness of Fit (R²)**: `{float(r2):.3f}`")
    if alpha is not None:
        md.append(f"- **Reliabilitas (Cronbach’s α)**: `{float(alpha):.3f}`  (items: {', '.join(items)})")
    md.append(f"- **Uji Perbedaan Antar Cluster**: {stats_line}")
    md.append(f"- **Power Analysis (target)**: {power_line}")
    md.append("\n> Catatan: Summary ini dibuat otomatis dari JSON (regresi, reliabilitas, uji beda, power).")

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out,"w") as f:
        f.write("\n".join(md))
    print("OK ->", args.out)
