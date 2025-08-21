import argparse
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
import json

def main():
    parser = argparse.ArgumentParser(description="Survey Analysis DPPT → Business Impact")
    parser.add_argument("--csv", required=True, help="Path ke file CSV survey")
    parser.add_argument("--out", required=True, help="Path output JSON hasil analisis")
    args = parser.parse_args()

    # Load data
    df = pd.read_csv(args.csv)

    # Feature & target
    X = df[["dppt_data", "dppt_process", "dppt_people", "dppt_technology"]]
    y = df["business_impact"]

    # Clustering
    kmeans = KMeans(n_clusters=3, random_state=42, n_init="auto").fit(X)
    df["cluster"] = kmeans.labels_

    cluster_summary = df.groupby("cluster")[["dppt_data","dppt_process","dppt_people","dppt_technology","business_impact"]].mean().to_dict()

    # Regression
    model = LinearRegression().fit(X, y)
    coefficients = dict(zip(X.columns, model.coef_))
    r2 = model.score(X, y)

    # Output JSON
    results = {
        "cluster_summary": cluster_summary,
        "regression": {
            "coefficients": coefficients,
            "intercept": model.intercept_,
            "r2_score": r2
        }
    }

    with open(args.out, "w") as f:
        json.dump(results, f, indent=2)

    print(f"Hasil analisis tersimpan di {args.out}")

if __name__ == "__main__":
    main()
