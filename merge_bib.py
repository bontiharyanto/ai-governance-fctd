import bibtexparser

# Daftar file .bib yang mau digabung
input_files = [
    "docs/references.bib",
    "docs/references_full.bib"
]

output_file = "docs/site-content/references_all.bib"

# Dictionary untuk menampung entry unik
entries_dict = {}

for bibfile in input_files:
    with open(bibfile, "r", encoding="utf-8") as f:
        bib_database = bibtexparser.load(f)
        for entry in bib_database.entries:
            key = entry["ID"].lower()
            if key not in entries_dict:
                entries_dict[key] = entry
            else:
                print(f"⚠️ Duplikat ditemukan, skip: {key}")

# Gabungkan hasil ke dalam satu BibDatabase
merged_bib = bibtexparser.bibdatabase.BibDatabase()
merged_bib.entries = list(entries_dict.values())

# Simpan hasil merge
with open(output_file, "w", encoding="utf-8") as f:
    bibtexparser.dump(merged_bib, f)

print(f"✅ Merge selesai! Total {len(merged_bib.entries)} entries disimpan di {output_file}")

