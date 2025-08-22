SHELL := /bin/zsh
PATH := $(HOME)/.local/bin:$(PATH)

MKDOCS ?= $(HOME)/.local/bin/mkdocs
PORT ?= 9000
MSG ?= "chore: update docs site"

REMOTE_URL := $(shell git config --get remote.origin.url)
OWNER := $(shell basename -s .git $$(dirname $(REMOTE_URL)))
REPO  := $(shell basename -s .git $(REMOTE_URL))
PAGES_URL := https://$(OWNER).github.io/$(REPO)/

.PHONY: updates docs serve kill-port deploy gh-pages-open ship

updates:
	python3 scripts/gen_updates.py

docs: updates
	$(MKDOCS) build -f docs/mkdocs.yml

serve: updates
	$(MKDOCS) serve -f docs/mkdocs.yml -a 127.0.0.1:$(PORT)

kill-port:
	@echo "Killing process on port $(PORT) (if any)…"
	-@lsof -ti :$(PORT) | xargs -r kill -9

deploy: updates
	@git add -A
	@git commit -m "$(MSG)" || echo "⚠️  No changes to commit"
	@git push origin main
	@echo "✅ Docs pushed. GitHub Actions akan membangun & deploy ke Pages."

gh-pages-open:
	@echo "🌐 Opening $(PAGES_URL)"
	@if [ "$$(uname -s)" = "Darwin" ]; then \
		open "$(PAGES_URL)"; \
	else \
		( command -v xdg-open >/dev/null && xdg-open "$(PAGES_URL)" ) || echo "$(PAGES_URL)"; \
	fi

WAIT ?= 45
ship: deploy
	@echo "⏳ Menunggu $(WAIT) detik agar GitHub Actions build selesai..."
	@sleep $(WAIT)
	$(MAKE) gh-pages-open.PHONY: research
research:
	python tools/ai_analysis/survey_analysis.py --csv data/sample_survey.csv --out results_survey.json
	python tools/ai_analysis/visualize_survey.py --csv data/sample_survey.csv --results results_survey.json --outdir reports
	python tools/ai_analysis/reliability.py --csv data/sample_survey.csv --out reliability.json
	~/.local/bin/mkdocs build -f docs/mkdocs.yml

.PHONY: research-sync
research-sync:
	python tools/ai_analysis/sync_reports.py
	~/.local/bin/mkdocs build -f docs/mkdocs.yml

