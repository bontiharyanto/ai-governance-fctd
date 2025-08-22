# ==== Build & Deploy MkDocs ====

# Ubah variabel ini jika perlu
PORT ?= 9011
BASE_PORT ?= 9011
MKDOCS ?= mkdocs               # atau override saat run: make serve MKDOCS=~/.local/bin/mkdocs
MKCONF ?= docs/mkdocs.yml

.PHONY: deploy serve serve-auto

deploy:
	@echo "🚀 Build & Deploy ke GitHub Pages..."
	$(MKDOCS) build -f $(MKCONF)
	$(MKDOCS) gh-deploy -f $(MKCONF) -b gh-pages --force
	@echo "✅ Selesai! Cek: https://bontiharyanto.github.io/ai-governance-fctd/"

# Kill bila port dipakai, lalu serve
serve:
	@port=$(PORT); \
	if lsof -i :$$port -sTCP:LISTEN >/dev/null 2>&1; then \
	  pid=$$(lsof -ti tcp:$$port); \
	  echo "⚠️  Port $$port in use by PID $$pid — killing..."; \
	  kill -9 $$pid || true; \
	  sleep 1; \
	fi; \
	echo "🌐 Starting MkDocs on http://127.0.0.1:$$port"; \
	$(MKDOCS) serve -f $(MKCONF) -a 127.0.0.1:$$port

# Cari port kosong mulai dari BASE_PORT, lalu serve
serve-auto:
	@p=$(BASE_PORT); \
	while lsof -i :$$p -sTCP:LISTEN >/dev/null 2>&1; do p=$$((p+1)); done; \
	if [ $$p -gt 65535 ]; then echo "No free port ≤ 65535"; exit 1; fi; \
	echo "🔎 Found free port: $$p"; \
	echo "🌐 Starting MkDocs on http://127.0.0.1:$$p"; \
	$(MKDOCS) serve -f $(MKCONF) -a 127.0.0.1:$$p
