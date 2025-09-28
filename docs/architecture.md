# 🧠 Threat Detection System Architecture

## 📦 Overview

This system is a modular, production-ready ML pipeline for detecting cybersecurity threats from log data. It is designed for scalability, maintainability, and integration into enterprise environments.

---

## 🧱 Core Modules

| Module              | Responsibility                                      |
|---------------------|-----------------------------------------------------|
| `config.py`         | Centralized configuration (paths, thresholds)       |
| `data_loader.py`    | Log ingestion and preprocessing                     |
| `feature_engineering.py` | Feature extraction from structured/unstructured logs |
| `model.py`          | ML model training, saving, loading                  |
| `detector.py`       | Threat detection using trained model                |
| `alert.py`          | Alerting via console and webhook                    |
| `main.py`           | Orchestrates full pipeline                          |
| `api.py`            | REST interface for external triggers                |
| `snowflake_ingest.py` | Optional: batch log export to Snowflake           |

---

## 🔄 Data Flow

1. **Log Ingestion**: Raw logs loaded from CSV or API
2. **Preprocessing**: Cleans nulls, parses timestamps
3. **Feature Engineering**: Extracts time/IP/message-based signals
4. **Model Training**: Isolation Forest trained on features
5. **Threat Detection**: Flags anomalies (-1) vs normal (1)
6. **Alerting**: Sends alerts via console/webhook
7. **Optional Export**: Logs pushed to Snowflake for analytics

---

## ☸️ Deployment Stack

- **Docker**: Containerized runtime
- **Helm**: Kubernetes packaging
- **Ansible**: Multi-node provisioning
- **Kubernetes**: Scalable orchestration
- **Snowflake**: Long-term log storage

---

## 🧪 Testing Strategy

- Unit tests for each module (`tests/`)
- CI pipeline via GitHub Actions
- Manual API testing via `curl` or Postman

---

## 📈 Future Enhancements

- Threat severity scoring
- Role-based access control
- Real-time log streaming
- SIEM integration
- Dashboard UI

---

## 🧩 Design Principles

- **Modularity**: Each component is independently testable
- **Scalability**: Supports horizontal scaling via K8s
- **Observability**: Logging and alerting built-in
- **Security**: Secrets via `.env`, optional RBAC
