SHELL := /bin/zsh
PATH := $(HOME)/.local/bin:$(PATH)

MKDOCS ?= $(HOME)/.local/bin/mkdocs
PORT ?= 9000
MSG ?= "chore: update docs site"

.PHONY: updates docs serve kill-port deploy

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
