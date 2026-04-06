# Makefile for Threat Detection System

.PHONY: install test run docker-build docker-run clean

install:
	pip install -r Requirements.txt

test:
	pytest tests/

run:
	python main.py

docker-build:
	docker build -t threat-detector .

docker-run:
	docker run --rm -p 8000:8000 threat-detector

clean:
	find . -type f -name "*.pyc" -delete
	rm -rf __pycache__/
