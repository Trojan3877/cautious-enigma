# main.py

from data_loader import load_log_data, preprocess_logs
from feature_engineering import extract_features
from detector import detect_threats
from alert import send_console_alert, send_webhook_alert
from model import train_model, save_model

def run_pipeline():
    # Step 1: Load and preprocess logs
    raw_logs = load_log_data()
    clean_logs = preprocess_logs(raw_logs)

    # Step 2: Extract features
    features = extract_features(clean_logs)

    # Step 3: Train model (optional — can be skipped if model already trained)
    model = train_model(features)
    if model:
        save_model(model)

    # Step 4: Detect threats
    threat_indices = detect_threats(features)

    # Step 5: Send alerts
    send_console_alert(threat_indices)
    send_webhook_alert(threat_indices)

if __name__ == "__main__":
    run_pipeline()
