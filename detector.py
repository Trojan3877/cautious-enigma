# detector.py

import logging
from model import load_model
from config import LOG_LEVEL

logging.basicConfig(level=LOG_LEVEL)

def detect_threats(features):
    if features.empty:
        logging.warning("Empty feature set received for detection.")
        return []

    model = load_model()
    if model is None:
        logging.error("No model available for detection.")
        return []

    predictions = model.predict(features)
    # IsolationForest: -1 = anomaly, 1 = normal
    threat_indices = [i for i, pred in enumerate(predictions) if pred == -1]
    logging.info(f"Detected {len(threat_indices)} potential threats.")
    return threat_indices
