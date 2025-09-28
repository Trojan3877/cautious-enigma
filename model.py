# model.py

import logging
import joblib
from sklearn.ensemble import IsolationForest
from config import MODEL_PATH, RANDOM_SEED, LOG_LEVEL

logging.basicConfig(level=LOG_LEVEL)

def train_model(X):
    if X.empty:
        logging.warning("Empty feature set received for training.")
        return None

    model = IsolationForest(random_state=RANDOM_SEED, contamination=0.1)
    model.fit(X)
    logging.info("Model training complete.")
    return model

def save_model(model, path=MODEL_PATH):
    try:
        joblib.dump(model, path)
        logging.info(f"Model saved to {path}")
    except Exception as e:
        logging.error(f"Failed to save model: {e}")

def load_model(path=MODEL_PATH):
    try:
        model = joblib.load(path)
        logging.info(f"Model loaded from {path}")
        return model
    except Exception as e:
        logging.error(f"Failed to load model: {e}")
        return None
