# feature_engineering.py

import pandas as pd
import logging
from config import LOG_LEVEL

logging.basicConfig(level=LOG_LEVEL)

def extract_features(df):
    if df.empty:
        logging.warning("Empty DataFrame received for feature extraction.")
        return pd.DataFrame()

    features = pd.DataFrame()

    # Example: time-based features
    if 'timestamp' in df.columns:
        df['hour'] = df['timestamp'].dt.hour
        features['hour'] = df['hour']

    # Example: frequency of IP addresses
    if 'source_ip' in df.columns:
        ip_counts = df['source_ip'].value_counts()
        features['ip_freq'] = df['source_ip'].map(ip_counts)

    # Example: binary flag for suspicious keywords
    if 'message' in df.columns:
        features['suspicious_flag'] = df['message'].str.contains("unauthorized|failed|error", case=False, na=False).astype(int)

    logging.info("Feature extraction complete.")
    return features
