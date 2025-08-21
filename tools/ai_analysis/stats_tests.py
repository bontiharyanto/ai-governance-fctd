#!/usr/bin/env python3
import argparse, json, os
import numpy as np, pandas as pd
from sklearn.cluster import KMeans
from scipy import stats

DPPT = ["dppt_data","dppt_process","dppt_people","dppt_technology"]

def load_or_cluster(csv_path, results_path=None):
    df = pd.read_csv(csv_path)
    # dukung skema kolom alternatif
    if all(c in df.columns for c in DPPT):
        Xcols = DPPT
    else:
        Xcols = ["data","process","people","technology"]
    if "cluster" not in df.columns:
        km = KMeans(n_clusters=3, random_state=42, n_init="auto")
        df["cluster"] = km.fit_predict(df[Xcols])
    return df

def anova_or_ttest(df):
    groups = [g["business_impact"].values for _, g in df.groupby("cluster")]
    k = len(groups)
    if k <= 1:
        return {"type":"none","message":"Hanya 1 cluster, tidak bisa uji beda."}
    if k == 2:
        t, p = stats.ttest_ind(groups[0], groups[1], equal_var=False)
        return {"type":"ttest", "t": float(t), "p": float(p), "n_groups": k,
                "group_sizes": [int(len(g)) for g in groups]}
    # k >= 3
    f, p = stats.f_oneway(*groups)
    return {"type":"anova", "F": float(f), "p": float(p), "n_groups": k,
            "group_sizes": [int(len(g)) for g in groups]}

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="t-test/ANOVA antar cluster untuk Business Impact")
    ap.add_argument("--csv", required=True)
    ap.add_argument("--out", default="stats_tests.json")
    args = ap.parse_args()

    df = load_or_cluster(args.csv)
    res = anova_or_ttest(df)
    with open(args.out,"w") as f:
        json.dump(res, f, indent=2)
    print("OK ->", args.out, res)
