# Model Card — Customer Support RAG (FCTD)

## 1. Identitas Model
- **Nama:** Assistant CS RAG  
- **Versi:** v1.0 (Februari 2025)  
- **Pemilik Model:** Head of AI – FCTD  
- **Use Case:** Mendukung agen Customer Support dengan jawaban berbasis KB internal  
- **Lingkup:** Agen internal; jawaban akhir bisa diteruskan ke pelanggan  

## 2. Deskripsi & Tujuan
- **Tujuan utama:** Mempercepat penyelesaian tiket support, menurunkan Average Handling Time (AHT), meningkatkan Customer Satisfaction (CSAT).  
- **Jenis AI:** Large Language Model (LLM) + Retrieval-Augmented Generation (RAG)  
- **Lingkungan:** Layanan internal FCTD, diakses via dashboard CS  

## 3. Dataset & Data Sheet
- **Sumber:** Artikel help center, changelog produk, FAQ, KB internal  
- **Lisensi:** Semua konten dimiliki & berlisensi internal FCTD  
- **Data PII:** Tidak disimpan di index; semua PII disamarkan sebelum logging  
- **Retensi:** Log output 90 hari, dengan masking PII  

## 4. Evaluasi & Metrik
- **Kualitas Jawaban:**  
  - Exact Match (EM): 72% (target ≥ 70%)  
  - F1-score: 0.81 (target ≥ 0.8)  
- **Robustness:**  
  - Prompt-injection defense: 98.8% sukses ditangkal (target ≥ 98%)  
- **Bias:**  
  - Audit pada 5 segmen tiket → tidak ditemukan disparitas signifikan  
- **Latency:**  
  - p95 latency = 2.3s (target ≤ 2.5s)  

## 5. Batasan & Known Failure Modes
- **KB tidak lengkap:** Model bisa berusaha menjawab dengan generalisasi → fallback “I don’t know”  
- **Ambiguitas pertanyaan:** Model bisa memberikan jawaban kurang spesifik → butuh HITL  
- **Topik di luar lingkup:** Model diarahkan menjawab “pertanyaan di luar lingkup”  

## 6. Kontrol & Mitigasi
- **C-001 Prompt Management & Grounding** — Semua jawaban wajib cite minimal 1 sumber KB  
- **C-002 PII Redaction** — Masking otomatis input/output/log  
- **C-003 Vendor Security** — DPA + residency APAC + non-training guarantee  
- **C-004 Human-in-the-Loop** — Pertanyaan sensitif (refund, hukum) harus disetujui agen  
- **C-005 Drift Monitoring** — Alert bila metrik kualitas turun > 5%  

## 7. Operasionalisasi
- **Monitoring aktif:** Dashboard observabilitas (latensi, metrik kualitas, feedback 👍/👎)  
- **Incident response:** Playbook MIM-AI dengan eskalasi ke CS Lead & Legal  
- **Rollback:** Feature flag + alur jawaban manual sebagai fallback  
- **Review:** Bulanan oleh PUC + Head of AI + Risk L2  

## 8. Kepatuhan & Legal
- **UU PDP:** Dipatuhi (data PII hanya diproses dengan minimisasi & masking)  
- **DPIA:** Sudah dilakukan (tersimpan di folder compliance/)  
- **Kontrak Vendor:** DPA, SLA, audit rights sudah aktif  

## 9. Versi & Sejarah
- **v1.0 (Feb 2025):** Rilis perdana ke pilot CS team  
- **Planned v1.1:** Perluasan coverage KB + integrasi dengan chatbot eksternal  

---

