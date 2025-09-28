# config.py

# Paths
LOG_DATA_PATH = "data/logs.csv"
MODEL_PATH = "models/threat_model.pkl"

# Detection thresholds
ANOMALY_THRESHOLD = 0.7  # Adjust based on model calibration

# Alert settings
ALERT_EMAIL = "security@yourdomain.com"
ALERT_WEBHOOK_URL = "https://your-alert-endpoint.com/webhook"

# Logging
LOG_LEVEL = "INFO"

# Misc
RANDOM_SEED = 42
