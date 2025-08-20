# AI Impact Assessment (AIA) — Use Case: Customer Support RAG (FCTD)

## 1. Ringkasan Use Case
- **Nama & Owner:** "Assistant CS RAG" — Pemilik Use Case (PUC): Nina Prameswari (Customer Ops)  
- **Tujuan bisnis & KPI:** Turunkan AHT -20%, naikkan CSAT +10p, first-contact-resolution +15p  
- **Kategori risiko:** Tinggi (output ke klien eksternal, potensi halusinasi & kebocoran data)  
- **Jenis AI:** LLM + Retrieval-Augmented Generation (RAG) dengan grounding ke KB internal  
- **Lingkup pengguna:** Agen CS internal; sebagian jawaban dikirim ke pelanggan  

## 2. Data & Privasi
- **Sumber data & lisensi:** KB internal, FAQ produk, changelog, dan artikel help center berlisensi FCTD  
- **PII/sensitif:** Ya — nama, email, nomor akun; ditangani via masking & policy redaksi log  
- **Dasar pemrosesan (UU PDP):** Kontrak layanan & kepentingan sah; transparansi pada kebijakan privasi  
- **Minimisasi & retensi:** PII tidak disimpan di index; log output disimpan 90 hari (PII masked) lalu dihapus  
- **Transfer lintas batas:** Data tetap di region APAC; vendor LLM harus menyediakan residency APAC  
- **Logging:** Prompt, context source, dan output dengan hash ticket; PII redaction otomatis pada log  

## 3. Evaluasi Risiko & Kontrol
- **Risiko utama:** Halusinasi (R-001), Kebocoran data (R-002), Bias, Model drift (R-003), Prompt injection  
- **Kontrol diterapkan:**  
  - C-001 Prompt Management & Grounding (wajib citation + top-k sources)  
  - C-002 PII Redaction (pre-processing & post-processing)  
  - C-003 Vendor Security (DPA, data residency, penonaktifan training-by-default)  
  - C-004 Human-in-the-Loop (HITL) untuk kasus sensitif  
  - C-005 Drift & Quality Monitoring (alert ketika metrik turun > threshold)  
- **Eksperimen & hasil uji:**  
  - Kualitas jawaban: EM 72%, F1 0.81 pada 500 pertanyaan uji; target EM ≥ 70%, F1 ≥ 0.8  
  - Keamanan: 250 prompt-injection tests → 98.8% ditangkal (target ≥ 98%)  
  - Bias: tidak ada disparitas signifikan antar segmen tiket; tinjau bulanan  
- **Batasan/failure modes:** KB tidak lengkap → model berusaha menggeneralisasi; gunakan fallback "I don’t know"  
- **Human-in-the-loop:** Kasus pembayaran/refund/keluhan hukum harus disetujui agen manusia  

## 4. Kepatuhan & Legal
- **DPIA diperlukan?** Ya — ada PII & dampak pelanggan; lampirkan DPIA  
- **Kewajiban vendor:** DPA ditandatangani; residency APAC; audit rights; no training on our data  
- **Hak IP:** Materi KB milik FCTD; API/model vendor sesuai lisensi  

## 5. Operasi & Monitoring
- **SLO & guardrail:** Halusinasi ≤ 2% sampel audit mingguan; latency p95 ≤ 2.5s; coverage citation ≥ 95%  
- **Observabilitas:** Dashboard tracing (prompt, context, output, sources, latensi), feedback tombol 👍/👎, tagging isu  
- **Incident response:** Playbook MIM-AI; komunikasi ke CS Lead & Legal bila ada pelanggaran PII  
- **Rollback & kill-switch:** Sediakan toggle feature flag & routing ke alur jawaban manual  
- **Review berkala:** Bulanan (PUC + Head of AI + Risk L2)  

## 6. Persetujuan
- **L1 (Tim Produk/AI):** …………………………… Tanggal: …………  
- **L2 (Risk & Compliance):** …………………………… Tanggal: …………  
- **L3 (Internal Audit, bila relevan):** …………………………… Tanggal: …………  

