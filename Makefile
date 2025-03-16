PHONY: test
test:
	@echo "tests started"
	@set PYTHONPATH=. && python -m pytest -v

PHONY: check
check: test
	isort .
	black .
	flake8 .