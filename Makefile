# Diretório(s) para aplicar o lint
SOURCES = .

style:
	ruff --fix $(SOURCES)

install:
	pip install -r requirements.txt

run:
	python snake.py

.PHONY: style install run
