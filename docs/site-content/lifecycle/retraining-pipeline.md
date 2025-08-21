# 🔁 Retraining Pipeline (Continuous Improvement)

Pipeline retraining memastikan model tetap relevan saat distribusi data berubah.

## Tujuan
- Menjaga performa (accuracy, fairness, robustness) terhadap data terbaru.
- Memenuhi **COBIT MEA01** (monitoring) & **NIST AI RMF – Manage**.

## Arsitektur Tingkat Tinggi
1. **Data Ingestion** → validasi skema, PII redaction (UU PDP).  
2. **Feature Store Update** → versioning & lineage.  
3. **Training Orchestrator** → pipeline terjadwal (Airflow/Kubeflow).  
4. **Evaluation Gate** → metrik utama + fairness & drift check.  
5. **Model Registry** → promosi dari *staging* → *prod* (policy-based).  
6. **Canary Release** → observasi dampak sebelum full rollout.  

## Kontrol Kunci
- **Data Validation** (Great Expectations, TFX)  
- **Bias/Fairness Testing** (SHAP/LIME, fairness metrics)  
- **Approval Workflow** (RACI: Model Owner A, MLOps R, DPO/Compliance C, Mgmt I)

## SLA & SLO
- SLA evaluasi ≤ 2 jam / model.  
- SLO drift alert ≤ 15 menit sejak anomali terdeteksi.

## Referensi
- NIST AI RMF (Measure, Manage) – 2023  
- ISACA COBIT 2019 (MEA01, BAI07)  
- TOGAF ADM (Architecture Change Management)  
