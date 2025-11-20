# 🛡️ AI-Powered Threat Detection System

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Production%20API-009688?logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Ready-0db7ed?logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Deployable-326ce5?logo=kubernetes)
![Helm](https://img.shields.io/badge/Helm-Charts-0f1689?logo=helm)
![Terraform](https://img.shields.io/badge/Terraform-IaC-7B42BC?logo=terraform)
![MLflow](https://img.shields.io/badge/Model%20Registry-Custom-green?logo=mlflow)
![CI/CD](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-black?logo=githubactions)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)



## 🚨 Overview
Cautious Enigma is an enterprise-grade ML system designed to classify vehicle safety risk using structured sensor data.
The project includes:

Full L6-level ML architecture

Production inference API built with FastAPI

Model Registry with versioning & SHA256 fingerprints

Preprocessing Pipeline (training + inference consistency)

Training Orchestrator (Airflow/Kubeflow ready)

Batch & real-time inference pipelines

Kubernetes-ready deployment stack (Docker + Helm + Terraform)

CI/CD compatible

## 🔧 Features
- Log ingestion and preprocessing
- Feature engineering for anomaly detection
- Isolation Forest-based threat classification
- Real-time alerting via console and webhook
- Configurable pipeline with modular components
- Ready for CI/CD and containerization

## 🧠 Technologies
- Python 3.9+
- Scikit-learn
- Pandas, NumPy
- Flask (optional API)
- Joblib
- Docker (optional)
- GitHub Actions (optional CI)

## 📁 Project Structure
cautious-enigma/
│
├── app/
│   ├── api.py             # FastAPI server
│   └── server.py          # Uvicorn entrypoint
│
├── models/
│   ├── baseline_model.py  # Baseline ML classifier
│   ├── inference.py       # Production inference engine
│   └── model_trainer.py   # Training orchestrator
│
├── pipelines/
│   ├── preprocess.py      # Full preprocessing pipeline
│   ├── train_pipeline.py  # End-to-end training DAG
│   └── inference_pipeline.py
│
├── utils/
│   ├── config.py
│   ├── data_loader.py
│   ├── logger.py
│   └── model_registry.py
│
├── config/
│   └── config.yaml
│
└── Dockerfile


                  ┌──────────────────────────┐
                  │        config.yaml        │
                  └─────────────┬────────────┘
                                │
              ┌─────────────────▼──────────────────┐
              │       Data Loader (utils/)         │
              └─────────────────┬──────────────────┘
                                │
                  ┌─────────────▼─────────────┐
                  │   Preprocess Pipeline     │
                  │ (training + inference)    │
                  └─────────────┬─────────────┘
                                │
                ┌───────────────▼────────────────┐
                │         Model Trainer           │
                │ (Pipeline + Evaluation + Save)  │
                └───────────────┬────────────────┘
                                │
                  ┌─────────────▼─────────────┐
                  │     Model Registry         │
                  │ (v1, v2, v3 + SHA256 hash) │
                  └─────────────┬─────────────┘
                                │
                    ┌───────────▼────────────────┐
                    │       Inference Engine      │
                    └───────────┬────────────────┘
                                │
                ┌───────────────▼─────────────────┐
                │             FastAPI              │
                │  /predict   /batch_predict       │
                │  /health    /ready    /live      │
                └──────────────────────────────────┘

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/yourusername/threat-detection-system.git
cd threat-detection-system

# Install dependencies
pip install -r requirements.txt

# Run the pipeline
python main.py
pytest tests/
docker build -t threat-detector .
docker run threat-detector
ALERT_WEBHOOK_URL=https://your-alert-endpoint.com/webhook
ALERT_EMAIL=security@yourdomain.com

## 📊 System Flowchart

```mermaid
flowchart TD
    A[Start: Log Data Ingestion] --> B[Preprocessing]
    B --> C[Feature Extraction]
    C --> D[Model Training / Loading]
    D --> E[Threat Detection]
    E --> F{Threats Found?}
    F -- Yes --> G[Send Alerts (Console/Webhook)]
    F -- No --> H[Log Normal Activity]
    G --> I[End]
    H --> I[End]


This flowchart shows:
- The modular pipeline from ingestion to alerting
- Decision logic for threat detection
- Clear separation of responsibilities

---

### 🧱 Next-Level Additions (Post-Flowchart)

Once the flowchart is in place, here’s what we’ll add next:

#### 🐳 Dockerfile
Containerize the app for portability and deployment.

#### ⚓ Helm Chart
Package your app for Kubernetes with customizable values.

#### 🧰 Ansible Playbook
Automate deployment across environments (e.g., dev, staging, prod).

#### ☸️ Kubernetes Manifests
Define pods, services, and deployments for scalable orchestration.

#### ❄️ Snowflake Integration
Optional: Stream logs into Snowflake for long-term storage and analytics.

#### 🧪 Advanced Files
- `tests/` with unit and integration tests
- `.env` with secrets (used via `python-dotenv`)
- `.github/workflows/ci.yml` for GitHub Actions
- `Makefile` for CLI automation
- `docs/architecture.md` for system design rationale

