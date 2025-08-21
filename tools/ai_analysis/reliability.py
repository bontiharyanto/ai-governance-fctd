#!/usr/bin/env python3
import argparse, pandas as pd, numpy as np, json

def cronbach_alpha(df):
    k = df.shape[1]
    variances = df.var(axis=0, ddof=1)
    total_var = df.sum(axis=1).var(ddof=1)
    return float((k/(k-1))*(1 - variances.sum()/total_var))

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Cronbach's Alpha for DPPT items")
    ap.add_argument("--csv", required=True, help="CSV with dppt_* columns")
    ap.add_argument("--out", default="reliability.json")
    args = ap.parse_args()

    df = pd.read_csv(args.csv)
    cols_dppt = [c for c in df.columns if c.startswith("dppt_")] or ["data","process","people","technology"]
    sub = df[cols_dppt]
    alpha = cronbach_alpha(sub)
    out = {"alpha": round(alpha, 4), "items": cols_dppt}
    with open(args.out,"w") as f: json.dump(out, f, indent=2)
    print("OK ->", args.out, out)
