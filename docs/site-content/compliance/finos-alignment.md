# 🔗 FINOS Alignment: FCTD ↔ FINOS ↔ NIST AI RMF ↔ Regulasi RI

Halaman ini memetakan kerangka **FCTD (DPPT)** ke domain-domain yang umum diadopsi komunitas **FINOS AI Governance Framework**, serta mengaitkannya dengan **NIST AI RMF** dan **regulasi Indonesia**.

## 1) Matriks Penyelarasan

| Domain FINOS (umum) | FCTD (DPPT) | NIST AI RMF (Core) | Regulasi RI (contoh) | Bukti/Artefak |
|---|---|---|---|---|
| **Governance & Oversight** | Policy, People | **Govern** | UU PDP, POJK, STRANAS AI | Charter dewan AI, RACI, keputusan kebijakan |
| **Policies & Standards** | Policy | **Govern/Manage** | UU PDP, ISO 42001 | Kebijakan AI, SOP, standar coding/model |
| **Risk Management** | Process, Policy | **Manage/Measure** | POJK 38/2016 | Risk Register, KRI, mitigasi, exception log |
| **Lifecycle & MLOps** | Process, Technology | **Map/Manage** | — | Pipeline ML, CI/CD, Model Registry |
| **Data Governance** | Data, Policy | **Map/Measure** | UU PDP, Permenkes 24/2022 | DDP, klasifikasi data, DPIA/AIA |
| **Model Dev & Testing** | Technology, Process | **Measure/Manage** | — | Test plan, bias tests, robustness report |
| **Security & Privacy** | Technology, Policy | **Manage** | UU PDP, POJK | DLP, PII redaction, IAM, audit trail |
| **Transparency & Explainability** | People, Policy | **Measure/Manage** | — | Model card, datasheet, explainability memo |
| **Operations & Monitoring** | Process, Technology | **Manage/Measure** | — | SLO/SLI, drift monitor, rollback plan |
| **Third-party & Procurement** | Policy, Process | **Govern/Manage** | UU PDP (joint-controller/processor) | SLA, DPIA vendor, due diligence |

> Catatan: Domain FINOS di atas merupakan pengelompokan umum yang selaras praktik FINOS/industri (governance, policies, risk, lifecycle, data, testing, security, transparency, operations, third-party). Gunakan ini sebagai **crosswalk** untuk audit internal.

## 2) Checklist Implementasi (Ringkas)

- Dewan tata kelola AI & **RACI** disahkan  
- Kebijakan AI (scope, risk taxonomy, escalation)  
- **Risk Register** aktif + KRI dan mitigasi  
- **AIA/DPIA** untuk use-case berdampak tinggi  
- **Dataset governance** (kualitas, lineage, lisensi)  
- **Bias & robustness testing** terdokumentasi  
- **PII protection** (pseudonymization/redaction)  
- **Model registry** beserta versioning & approvals  
- **Monitoring** (drift, hallucination, misuse) + rollback  
- **Vendor oversight** (SLA, audit hak, data localization)

## 3) Bukti Kepatuhan yang Direkomendasikan

- Kebijakan & SOP (signed)  
- AIA/DPIA per use-case  
- Datasheet & Model Card  
- Red-Teaming / Adversarial test report  
- Audit trail & change log (CI/CD)  
- Bukti training & kompetensi peran kritikal  


[AI Impact Assessment (AIA)](../templates/ai-impact-assessment-template.md)
[DPIA](../templates/dpia-template.md)
[Model Card](../templates/model-card-template.md)
[Datasheet](../templates/datasheet-template.md)

[Contoh AIA (Bank)](../examples/bank-credit-scoring/aia-example.md)
[Contoh DPIA (Bank)](../examples/bank-credit-scoring/dpia-example.md)
[Contoh Model Card (Bank)](../examples/bank-credit-scoring/model-card-example.md)
[Contoh Datasheet (Bank)](../examples/bank-credit-scoring/datasheet-example.md)

