# AI Impact Assessment (AIA) – Template
<!-- Akan diisi detail setelah struktur selesai -->
# AI Impact Assessment (AIA) — FCTD

## 1. Ringkasan Use Case
- **Nama & Owner:**  
- **Tujuan bisnis & KPI:**  
- **Kategori risiko (rendah/sedang/tinggi):**  
- **Jenis AI:** (LLM/RAG/klasik/CV/NLP lain)  
- **Lingkup pengguna:** (internal/eksternal/kritis)

## 2. Data & Privasi
- **Sumber data & lisensi:**  
- **PII/sensitif:** (ya/tidak; jenis PII)  
- **Dasar pemrosesan (UU PDP):** persetujuan/kontrak/kewajiban hukum/dst  
- **Minimisasi & retensi:** (kapan dihapus/di-anonim)  
- **Transfer lintas batas:** lokasi data, proteksi yang diterapkan  
- **Logging:** input/output/model telemetry (kebijakan redaksi/mascarade PII)

## 3. Evaluasi Risiko & Kontrol
- **Risiko utama:** (mis. halusinasi, data leakage, bias, drift, keamanan prompt)  
- **Kontrol yang diterapkan (ID kontrol):** C-001 Prompt Management, C-002 PII Redaction, C-004 HITL, C-005 Drift Monitoring, dst  
- **Eksperimen & hasil uji:** metrik kualitas (exact match/F1/ROUGE), bias (DP/EO), robustness (adversarial), keamanan (prompt injection/red team)  
- **Batasan model & failure modes:**  
- **Human-in-the-loop:** kapan manusia harus menyetujui/meninjau

## 4. Kepatuhan & Legal
- **DPIA diperlukan?** (ya/tidak + alasan)  
- **Kewajiban kontraktual/vendor:** DPA, SLA, sub-processor, audit rights  
- **Hak IP & attribution:** data pelatihan, model, kode

## 5. Operasi & Monitoring
- **SLO & guardrail:** ambang metrik kualitas, tingkat halusinasi maksimum, latency  
- **Observabilitas:** dashboard, alert, pelabelan user feedback  
- **Incident response:** playbook, MIM, komunikasi ke stakeholder  
- **Rollback & kill-switch:** kondisi pemicu & prosedur  
- **Review berkala:** (bulanan/kuartalan) + pemilik review

## 6. Persetujuan
- **L1 (Tim Produk/AI):** Nama & Tanggal  
- **L2 (Risk & Compliance):** Nama & Tanggal  
- **L3 (Internal Audit, bila relevan):** Nama & Tanggal

