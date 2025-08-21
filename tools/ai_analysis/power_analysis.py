#!/usr/bin/env python3
import argparse, json
from statsmodels.stats.power import TTestIndPower

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Power analysis (two-sample t-test)")
    ap.add_argument("--effect", type=float, default=0.5, help="Cohen's d, default=0.5 (sedang)")
    ap.add_argument("--alpha", type=float, default=0.05)
    ap.add_argument("--power", type=float, default=0.8)
    ap.add_argument("--ratio", type=float, default=1.0, help="n2/n1")
    ap.add_argument("--out", default="power.json")
    args = ap.parse_args()

    analysis = TTestIndPower()
    n = analysis.solve_power(effect_size=args.effect, alpha=args.alpha,
                             power=args.power, ratio=args.ratio, alternative='two-sided')
    out = {
        "effect_size": args.effect,
        "alpha": args.alpha,
        "power": args.power,
        "ratio": args.ratio,
        "min_sample_per_group": float(n),
        "min_total_samples": float(n*(1+args.ratio))
    }
    with open(args.out,'w') as f:
        json.dump(out, f, indent=2)
    print("OK ->", args.out, out)
