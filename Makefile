# Detect operating system
ifeq ($(OS),Windows_NT)
	SCRIPT_BOOTSTRAP := bootstrap.bat
    SCRIPT_RUN := run.bat
else
	SCRIPT_BOOTSTRAP := ./bootstrap.sh
    SCRIPT_RUN := ./run.sh
endif

.PHONY: bootstrap run check format
bootstrap:
	$(SCRIPT_BOOTSTRAP)

run:
	$(SCRIPT_RUN)

format:
	uv run ruff check --fix .
	uv run ruff format .

check:
	uv run ruff format --check .
	uv run ruff check .
