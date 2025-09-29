# benchmark.py

import time
import pandas as pd
from data_loader import preprocess_logs
from feature_engineering import extract_features
from model import train_model
from detector import detect_threats

df = pd.read_csv("data/sample_logs.csv")

start = time.time()
df_clean = preprocess_logs(df)
features = extract_features(df_clean)
model = train_model(features)
threats = detect_threats(features)
end = time.time()

print(f"Pipeline executed in {end - start:.2f} seconds")
print(f"Threats detected: {len(threats)}")
