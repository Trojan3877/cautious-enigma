# examples/example_pipeline.py

from data_loader import preprocess_logs
from feature_engineering import extract_features
from model import train_model
from detector import detect_threats
from alert import send_alert

import pandas as pd

# Load sample logs
df = pd.read_csv("data/sample_logs.csv")

# Run pipeline
df_clean = preprocess_logs(df)
features = extract_features(df_clean)
model = train_model(features)
threats = detect_threats(features)

# Alert
send_alert(threats)
