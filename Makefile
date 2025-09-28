# Makefile for Threat Detection System

.PHONY: install test run docker-build docker-run clean

install:
    pip install -r requirements.txt

test:
    pytest tests/

run:
    python main.py

docker-build:
    docker build -t threat-detector .

docker-run:
    docker run --rm threat-detector

clean:
    find . -type f -name "*.pyc" -delete
    rm -rf __pycache__/


make install        # Install dependencies
make test           # Run test suite
make run            # Execute pipeline
make docker-build   # Build Docker image
make docker-run     # Run container
make clean          # Remove cache files
