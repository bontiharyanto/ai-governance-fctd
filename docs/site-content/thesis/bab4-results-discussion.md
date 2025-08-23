# 📊 Bab 4 – Hasil & Pembahasan

## 4.1 Hasil Survei
Hasil survei terhadap **150 responden** yang berasal dari industri perbankan, jasa keuangan, kesehatan, dan teknologi informasi di Indonesia menunjukkan bahwa:
- **40%** responden berasal dari sektor perbankan & keuangan.
- **25%** responden berasal dari sektor kesehatan.
- **35%** berasal dari sektor IT & lainnya.
- Sekitar **30% perusahaan** telah mengimplementasikan AI, **40% dalam tahap uji coba**, dan **30% masih pada tahap perencanaan**.

Profil responden juga memperlihatkan dominasi perusahaan menengah–besar (≥ 250 pegawai), dengan mayoritas berlokasi di Jakarta, Surabaya, Bandung, dan Medan.

## 4.2 Analisis Clustering
Menggunakan metode **K-Means clustering**, responden terbagi menjadi tiga kelompok readiness AI Governance:
1. **Cluster A (High Readiness – 25%)**  
   Sudah memiliki tata kelola data, risk register AI, dan unit khusus AI Ethics.
2. **Cluster B (Moderate Readiness – 45%)**  
   Punya kebijakan dasar, tetapi implementasi teknis (seperti AIA/DPIA) masih terbatas.
3. **Cluster C (Low Readiness – 30%)**  
   Baru pada tahap eksplorasi, tanpa kebijakan formal terkait AI.

Visualisasi radar chart memperlihatkan bahwa dimensi **Policy** dan **People** masih lemah dibanding **Data**, **Process**, dan **Technology**.

## 4.3 Diskusi
Hasil ini konsisten dengan penelitian NIST (2023) yang menekankan bahwa **governance readiness** di negara berkembang cenderung rendah pada dimensi kebijakan [@NIST2023].  
Penerapan AI di Indonesia juga dipengaruhi oleh **regulasi sektoral (POJK 38/2016, UU PDP 2022)** yang menuntut kepatuhan data, namun belum seluruh organisasi siap secara infrastruktur.

**Kelebihan pendekatan** ini adalah mampu memetakan readiness secara kuantitatif. Namun, **kelemahan** utama terletak pada keterbatasan sampel yang berbasis self-assessment.

---

## 4.4 Crosswalk Kontrol → Evidence → Metrik

| Area    | Kontrol                         | Evidence (Bukti)                  | Metrik                          |
|---------|---------------------------------|-----------------------------------|---------------------------------|
| Data    | Penerapan Data Governance        | Dataset readiness, Policy Data    | % organisasi dengan kebijakan   |
| Process | Risk Management                  | Risk Register, Audit              | % risiko dengan mitigasi aktif  |
| People  | Awareness & Skill                | Hasil Survey Training             | Jam training/pegawai per tahun  |
| Tech    | Infrastruktur Cloud/On-Prem      | Audit TI, Arsitektur Infrastruktur| Rasio cloud vs on-premises      |
| Policy  | Kepatuhan UU PDP & POJK          | Dokumen Audit Compliance          | % kontrol comply                |

---

## 4.5 Implikasi
- **Regulator**: perlu mempercepat integrasi standar global (NIST AI RMF, COBIT, TOGAF) dengan regulasi nasional.  
- **Industri**: harus fokus pada *capacity building* SDM dan penyusunan AIA/DPIA.  
- **Akademisi**: perlu mengembangkan metodologi evaluasi AI Governance berbasis konteks Indonesia.
