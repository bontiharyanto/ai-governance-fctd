# 🏛️ Operating Model & RACI

## 1) Struktur
- **AI Governance Board** (independen lintas fungsi)
- **Risk & Compliance** (PDP, audit, legal)
- **MLOps & Platform** (CI/CD, registry, monitoring)
- **Data Office** (quality, lineage, privacy)
- **Product & Domain SME** (ownership use-case)

## 2) RACI (contoh)

| Aktivitas | C | R | A | I |
|---|---|---|---|---|
| Kebijakan AI | Risk/Legal | GovSec | Board Chair | Semua |
| AIA/DPIA | Risk | Product Owner | CISO | Data Office |
| Bias testing | Data Science | QA/Testing | Head of DS | Compliance |
| Deploy model | MLOps | DS Engineer | Head of Eng | Product |
| Monitoring & rollback | MLOps | SRE | CTO | Board |

> C=Create, R=Responsible, A=Accountable, I=Informed
