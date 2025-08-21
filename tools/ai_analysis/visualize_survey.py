#!/usr/bin/env python3
import argparse, os, json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression

DPPT_COLS = ["dppt_data","dppt_process","dppt_people","dppt_technology"]

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def normalize_cluster_mean(cm):
    """Terima dict orientasi 'cluster-major' ATAU 'column-major', kembalikan cluster-major."""
    if not isinstance(cm, dict) or not cm:
        return {}

    keys = list(cm.keys())

    # Jika kunci tampak seperti kolom (dppt_...), berarti column-major: {col: {cluster: mean}}
    if any(k in DPPT_COLS for k in keys) or any(k in ["data","process","people","technology"] for k in keys):
        # Transpose ke cluster-major
        # siapkan daftar cluster dari salah satu kolom
        clusters = set()
        for col, sub in cm.items():
            if isinstance(sub, dict):
                clusters.update(sub.keys())
        out = {}
        # pakai urutan kolom dppt_ jika ada; fallback ke non-dppt
        cols = DPPT_COLS if any(k in DPPT_COLS for k in keys) else ["data","process","people","technology"]
        for c in clusters:
            row = {}
            for col in cols:
                val = cm.get(col, {}).get(c, 0)
                # normalisasi nama kolom ke dppt_
                if col == "data": col = "dppt_data"
                if col == "process": col = "dppt_process"
                if col == "people": col = "dppt_people"
                if col == "technology": col = "dppt_technology"
                row[col] = val
            out[str(c)] = row
        return out

    # Jika kunci tampak seperti id cluster ('0','1','2', ...): sudah cluster-major
    out = {}
    for k, v in cm.items():
        # pastikan subkeys pakai dppt_*
        if isinstance(v, dict):
            nv = {}
            for col, val in v.items():
                col2 = col
                if col == "data": col2 = "dppt_data"
                if col == "process": col2 = "dppt_process"
                if col == "people": col2 = "dppt_people"
                if col == "technology": col2 = "dppt_technology"
                nv[col2] = val
            out[str(k)] = nv
        else:
            out[str(k)] = v
    return out

def normalize_coefs(coefs):
    """Samakan nama koefisien ke dppt_* bila perlu."""
    out = {}
    for k, v in coefs.items():
        k2 = k
        if k == "data": k2 = "dppt_data"
        if k == "process": k2 = "dppt_process"
        if k == "people": k2 = "dppt_people"
        if k == "technology": k2 = "dppt_technology"
        out[k2] = v
    return out

def compute_from_csv(csv_path):
    df = pd.read_csv(csv_path)
    # dukung dua skema nama kolom
    if all(c in df.columns for c in DPPT_COLS):
        Xcols = DPPT_COLS
    elif all(c in df.columns for c in ["data","people","process","technology"]):
        Xcols = ["data","process","people","technology"]
    else:
        raise SystemExit("Kolom tidak ditemukan. Butuh dppt_* atau data/people/process/technology")

    X = df[Xcols].values
    y = df["business_impact"].values
    km = KMeans(n_clusters=3, random_state=42, n_init="auto").fit(X)
    df["cluster"] = km.labels_
    cluster_mean = df.groupby("cluster")[Xcols+["business_impact"]].mean().round(2).to_dict()

    # transpose jika perlu → cluster-major dan dppt_*
    cluster_mean = normalize_cluster_mean(cluster_mean)

    reg = LinearRegression().fit(df[Xcols], df["business_impact"])
    coefs = dict(zip(Xcols, reg.coef_.round(4)))
    coefs = normalize_coefs(coefs)
    r2 = float(round(reg.score(df[Xcols], df["business_impact"]),4))
    y_pred = reg.predict(df[Xcols])
    return cluster_mean, coefs, float(reg.intercept_), r2, df["business_impact"].values, y_pred

def load_results(results_path):
    with open(results_path, "r") as f:
        data = json.load(f)
    # v1: {"clusters_mean": {...}, "regression": {...}}
    if "clusters_mean" in data and "regression" in data:
        cm = normalize_cluster_mean(data["clusters_mean"])
        coefs = normalize_coefs(data["regression"]["coefficients"])
        intercept = float(data["regression"].get("intercept", 0.0))
        r2 = float(data["regression"].get("r2", data["regression"].get("r2_score", 0.0)))
        return cm, coefs, intercept, r2
    # v2: {"cluster_summary": {...}, "regression": {...}}
    if "cluster_summary" in data and "regression" in data:
        cm = normalize_cluster_mean(data["cluster_summary"])
        coefs = normalize_coefs(data["regression"]["coefficients"])
        intercept = float(data["regression"].get("intercept", 0.0))
        r2 = float(data["regression"].get("r2_score", data["regression"].get("r2", 0.0)))
        return cm, coefs, intercept, r2
    raise ValueError("results JSON tidak dikenali strukturnya")

def radar_chart(cluster_mean, out_png):
    labels = ["Data","Process","People","Technology"]
    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]

    plt.figure(figsize=(7,7))
    ax = plt.subplot(111, polar=True)
    ax.set_theta_offset(np.pi / 2); ax.set_theta_direction(-1)
    ax.set_thetagrids(np.degrees(angles[:-1]), labels)

    for k in sorted(cluster_mean.keys(), key=lambda x: int(x) if str(x).isdigit() else x):
        means = [cluster_mean[k].get(c,0) for c in ["dppt_data","dppt_process","dppt_people","dppt_technology"]]
        values = means + means[:1]
        ax.plot(angles, values, linewidth=2, label=f"Cluster {k}")
        ax.fill(angles, values, alpha=0.1)

    ax.set_title("Readiness Profile by Cluster (DPPT)")
    ax.set_rlabel_position(0)
    plt.legend(loc="upper right", bbox_to_anchor=(1.25, 1.1))
    plt.tight_layout()
    plt.savefig(out_png, dpi=160); plt.close()

def bar_coeffs(coefs, out_png):
    keys = ["dppt_data","dppt_process","dppt_people","dppt_technology"]
    vals = [coefs.get(k,0) for k in keys]
    names = ["Data","Process","People","Technology"]
    plt.figure(figsize=(7,4))
    plt.bar(names, vals)
    plt.title("Regression Coefficients (DPPT → Business Impact)")
    plt.ylabel("Coefficient")
    plt.tight_layout()
    plt.savefig(out_png, dpi=160); plt.close()

def scatter_pred(df_csv, out_png):
    df = pd.read_csv(df_csv)
    if all(c in df.columns for c in DPPT_COLS):
        X = df[DPPT_COLS]
    else:
        X = df[["data","process","people","technology"]]
    y = df["business_impact"]
    reg = LinearRegression().fit(X, y)
    y_pred = reg.predict(X)
    plt.figure(figsize=(6,6))
    plt.scatter(y, y_pred, alpha=0.7)
    mn = min(y.min(), y_pred.min()); mx = max(y.max(), y_pred.max())
    plt.plot([mn,mx],[mn,mx], linestyle="--")
    plt.title(f"Actual vs Predicted (R²={reg.score(X,y):.2f})")
    plt.xlabel("Actual Business Impact"); plt.ylabel("Predicted Business Impact")
    plt.tight_layout(); plt.savefig(out_png, dpi=160); plt.close()

def write_html(outdir, files):
    html_path = os.path.join(outdir, "index.html")
    with open(html_path, "w") as f:
        f.write("<html><head><meta charset='utf-8'><title>Survey Visualizations</title></head><body>")
        f.write("<h1>Survey Visualizations</h1>")
        for title, fn in files:
            f.write(f"<h2>{title}</h2><img src='{os.path.basename(fn)}' style='max-width:900px;width:100%;border:1px solid #eee;border-radius:8px'/>")
        f.write("</body></html>")
    return html_path

def main():
    ap = argparse.ArgumentParser(description="Visualize DPPT Survey")
    ap.add_argument("--csv", required=True, help="CSV path")
    ap.add_argument("--results", default=None, help="results_survey.json (optional)")
    ap.add_argument("--outdir", default="reports", help="output directory")
    args = ap.parse_args()

    ensure_dir(args.outdir)

    if args.results and os.path.exists(args.results):
        try:
            cluster_mean, coefs, intercept, r2 = load_results(args.results)
            scatter_pred(args.csv, os.path.join(args.outdir, "pred_vs_actual.png"))
        except Exception as e:
            print("Gagal membaca results JSON, hitung ulang dari CSV:", e)
            cluster_mean, coefs, intercept, r2, y, y_pred = compute_from_csv(args.csv)
            scatter_pred(args.csv, os.path.join(args.outdir, "pred_vs_actual.png"))
    else:
        cluster_mean, coefs, intercept, r2, y, y_pred = compute_from_csv(args.csv)
        scatter_pred(args.csv, os.path.join(args.outdir, "pred_vs_actual.png"))

    radar_png = os.path.join(args.outdir, "radar_clusters.png")
    coeff_png = os.path.join(args.outdir, "regression_coeffs.png")
    radar_chart(cluster_mean, radar_png)
    bar_coeffs(coefs, coeff_png)

    html = write_html(args.outdir, [
        ("Readiness Profile by Cluster", radar_png),
        ("Regression Coefficients", coeff_png),
        ("Actual vs Predicted", os.path.join(args.outdir, "pred_vs_actual.png"))
    ])
    print("Saved charts to:", args.outdir)
    print("Open:", html)

if __name__ == "__main__":
    main()
