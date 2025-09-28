# tests/test_pipeline.py

import pandas as pd
from data_loader import preprocess_logs
from feature_engineering import extract_features
from model import train_model
from detector import detect_threats

def test_preprocess_logs():
    raw = pd.DataFrame({
        'timestamp': ['2025-09-28 12:00:00', None],
        'source_ip': ['192.168.1.1', '192.168.1.2'],
        'message': ['login failed', 'unauthorized access']
    })
    clean = preprocess_logs(raw)
    assert not clean.isnull().values.any()
    assert 'timestamp' in clean.columns

def test_extract_features():
    df = pd.DataFrame({
        'timestamp': pd.to_datetime(['2025-09-28 12:00:00']),
        'source_ip': ['192.168.1.1'],
        'message': ['unauthorized access']
    })
    features = extract_features(df)
    assert 'hour' in features.columns
    assert 'ip_freq' in features.columns
    assert 'suspicious_flag' in features.columns

def test_model_training_and_detection():
    df = pd.DataFrame({
        'hour': [12, 13, 14],
        'ip_freq': [5, 3, 8],
        'suspicious_flag': [1, 0, 1]
    })
    model = train_model(df)
    assert model is not None
    threats = detect_threats(df)
    assert isinstance(threats, list)
