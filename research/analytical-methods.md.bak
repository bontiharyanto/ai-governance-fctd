# 🧪 Metode Analisis & Validasi

Bab ini menjelaskan **metodologi analisis**, mulai dari pemilihan metode statistik/ML, metrik evaluasi, hingga rencana validasi hasil. Tujuan utamanya adalah memastikan framework FCTD tidak hanya konseptual, tetapi dapat **diuji secara empiris**.

---

## Desain Analisis

Kerangka analisis dibangun di atas **DPPT (Data, Process, People, Technology, Policy)** dengan referensi standar **TOGAF, COBIT, NIST AI RMF**, dan regulasi (**UU PDP, POJK, STRANAS AI**).  
Tahap analisis dibagi menjadi:

1. **Deskriptif** – eksplorasi data survei & evidensi (mean, distribusi, korelasi).  
2. **Inferensial** – uji hipotesis melalui **regresi**, **clustering**, dan **korelasi**.  
3. **Evaluatif** – mengukur kinerja model menggunakan metrik akurasi & stabilitas.  
4. **Validatif** – pembuktian robustness dengan **cross-validation**, hold-out test, serta expert review.

---

## 1. Metode Analisis

### 🔹 1.2  Clustering
Digunakan untuk **mengelompokkan unit organisasi** berdasarkan tingkat kesiapan DPPT.

- Algoritma: **K-Means**  
- Input: skor readiness tiap dimensi DPPT (skala Likert 1–5).  
- Output: cluster (misalnya *low, medium, high readiness*).  
- Evaluasi: **Silhouette Score** dan **stability index** antar-run.

### 🔹 1.3  Regresi
Digunakan untuk **menguji hubungan kausal** antar-variabel.

- Model: **Linear Regression** & **Ridge Regression** (regularisasi).  
- Dependen: *AI Governance Maturity*, *Compliance Readiness*, *Business Impact*.  
- Independen: skor DPPT, regulatory fit, hasil cluster readiness.  
- Evaluasi: **R², RMSE, MAE**, serta uji signifikansi koefisien.

### 🔹 1.4  Korelasi & Reliabilitas
- **Pearson/Spearman Correlation** → untuk mengukur asosiasi antar-dimensi.  
- **Cronbach’s Alpha (α)** → untuk uji reliabilitas kuesioner (target ≥ 0.7).  
- **KMO & Bartlett’s Test** → validasi kelayakan analisis faktor.

---

## 2 Evaluasi & Metrik

| Domain | Metrik | Tujuan |
|--------|--------|--------|
| **Data** | completeness, accuracy, imbalance ratio | Kualitas data & fairness |
| **Process** | SLA kepatuhan, jumlah temuan audit | Maturitas proses |
| **People** | coverage pelatihan, role coverage | Kompetensi & kesadaran |
| **Technology** | RMSE/MAE/R², drift detection | Robustness model |
| **Policy** | jumlah DPIA, policy exception, auditability | Kepatuhan regulasi |
| **Outcome** | Governance maturity index, compliance readiness index, business impact (ROAI) | Efektivitas keseluruhan |

---

## 3. Validasi

1. **Hold-out validation** – 70% data untuk training, 30% untuk testing.  
2. **k-fold cross-validation** – k = 5 atau 10, untuk mengurangi bias sampling.  
3. **Stability test** – pengulangan clustering & regresi pada data bootstrap.  
4. **Expert review** – triangulasi hasil dengan penilaian ahli (governance, compliance, AI ethics).

---

## 4. Hipotesis Penelitian

- **H1:** Peningkatan kapabilitas DPPT → peningkatan AI Governance Maturity.  
- **H2:** Pemetaan DPPT ↔ NIST menurunkan AI risk & meningkatkan Compliance Readiness.  
- **H3:** Governance Maturity ↗ → Business Impact ↗.  
- **H4:** Regulatory fit memperkuat pengaruh DPPT terhadap outcome.

---

## 5. Instrumen & Pengumpulan Data

- **Survei readiness** (Likert 1–5, 30–50 item) mencakup tiap dimensi DPPT.  
- **Checklist evidensi** (kebijakan, model card, audit trail).  
- **Log MLOps/AI Ops** (drift, fairness, explainability metrics).  
- **Wawancara/FGD** (untuk validasi expert).

---

## 6. Ringkasan Alur Analisis

```mermaid
flowchart TD
  A[Data Survei & Evidensi] --> B[Preprocessing & Scoring DPPT]
  B --> C[Clustering (KMeans)]
  B --> D[Regresi (Linear/Ridge)]
  C & D --> E[Evaluasi (R², RMSE, Silhouette, Stability)]
  E --> F[Validasi (CV, hold-out, expert review)]
  F --> G[Outcome: Maturity • Compliance • Business Impact]
