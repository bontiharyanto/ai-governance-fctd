# Risk Register

## Kategori Risiko AI
Mengacu pada **NIST AI RMF** & **COBIT APO12**:

- **Risiko Privasi & Kebocoran Data** → UU PDP, POJK TI.
- **Risiko Bias & Diskriminasi** → NIST AI RMF: Fairness.
- **Risiko Model Drift** → STRANAS AI: monitoring jangka panjang.
- **Risiko Cybersecurity** → COBIT DSS05.
- **Risiko Kepatuhan Hukum** → UU PDP, UU ITE, regulasi sektor.

| ID | Risiko | Dampak | Probabilitas | Mitigasi | Framework Acuan |
|----|--------|---------|--------------|----------|-----------------|
| R1 | Kebocoran PII dari dataset | Tinggi | Sedang | Pseudonimisasi, masking, enkripsi | UU PDP, POJK |
| R2 | Bias algoritmik (gender/ras) | Tinggi | Sedang | Fairness testing, XAI | NIST AI RMF |
| R3 | Model drift | Sedang | Tinggi | Continuous Monitoring, retraining | STRANAS AI |
| R4 | Serangan adversarial | Tinggi | Rendah | Red teaming, penetration testing | NIST, COBIT |
| R5 | Non-compliance hukum | Tinggi | Sedang | Legal review, DPIA | UU PDP, POJK |

---
📖 **References**:
- NIST AI RMF 1.0 (2023)
- COBIT 2019 (APO12, DSS05)
- UU PDP No.27/2022
- POJK No.38/2016
