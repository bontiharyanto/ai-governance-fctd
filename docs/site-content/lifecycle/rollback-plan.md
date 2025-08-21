# ⏪ Rollback & Incident Response Plan

Rencana pemulihan cepat saat model menimbulkan risiko tinggi.

## Kapan Rollback
- Drift kritikal, pelanggaran privasi, bias parah, atau kegagalan fungsional.

## Strategi
1. **Blue/Green**: revert ke versi stabil di *green* environment.  
2. **Canary Disable**: matikan canary & rute trafik ke model stabil.  
3. **Kill Switch**: nonaktifkan endpoint model.  
4. **Feature Flag**: matikan fitur yang memanggil model.  

## Runbook Insiden
- *Detect* → *Triage (SEV level)* → *Contain* → *Eradicate* → *Recover* → *Postmortem*.  
- Komunikasi: notifikasi regulator (jika terkait PII) sesuai UU PDP.

## Peran (RACI)
- **A**: Model Owner / Product Owner  
- **R**: MLOps / SRE  
- **C**: DPO, Compliance, Security  
- **I**: Manajemen, Stakeholder terkait

## Referensi
- NIST AI RMF (Manage)  
- COBIT DSS02 (Service Requests & Incidents), DSS04 (Continuity)  
- POJK 13/2021 (Tata Kelola TI & Kontinuitas Layanan)
