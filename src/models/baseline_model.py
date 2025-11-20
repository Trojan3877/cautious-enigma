"""
baseline_model.py — L5/L6 Production-Grade ML Model

This module defines a baseline model architecture with:
✔ Config-driven hyperparameters
✔ Scaling + model training pipeline
✔ Logging for observability
✔ Automatic model registry saving
✔ Clean train() and predict() APIs
"""

import logging
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

from utils.config import get_config
from utils.model_registry import get_registry

logger = logging.getLogger("BaselineModel")
logger.setLevel(logging.INFO)


class BaselineClassifier:
    """
    A production-grade classifier implementation.
    
    Handles:
    - Preprocessing
    - Training
    - Evaluation
    - Model registry saving
    - Inference
    """

    def __init__(self):
        self.cfg = get_config()
        self.registry = get_registry()

        # Load model params from config
        lr_params = self.cfg.get("model.lr_params", {})

        # Full preprocessing + model training pipeline
        self.pipeline = Pipeline(
            steps=[
                ("scaler", StandardScaler()),
                ("classifier", LogisticRegression(**lr_params)),
            ]
        )

    def train(self, X_train, y_train):
        """Train model using provided data."""
        logger.info("Training Baseline Classifier...")

        try:
            self.pipeline.fit(X_train, y_train)
            logger.info("[TRAINING SUCCESS] Model pipeline fitted successfully.")
        except Exception as e:
            logger.error(f"[TRAINING ERROR] {e}")
            raise

        # Save model after training
        metadata = self.registry.save_model(self.pipeline, "baseline_classifier")
        logger.info(f"[MODEL REGISTERED] {metadata}")

        return metadata

    def evaluate(self, X_test, y_test):
        """Evaluate model on held-out dataset."""
        logger.info("Evaluating Baseline Classifier...")

        preds = self.pipeline.predict(X_test)
        acc = accuracy_score(y_test, preds)

        logger.info(f"[ACCURACY] {acc:.4f}")
        logger.info("\n" + classification_report(y_test, preds))

        return {
            "accuracy": acc,
            "report": classification_report(y_test, preds, output_dict=True),
        }

    def predict(self, X):
        """Make predictions using the trained model."""
        return self.pipeline.predict(X)

    def load_latest(self):
        """Load the latest registered model."""
        logger.info("[LOADING] Latest version of baseline_classifier")
        self.pipeline = self.registry.load_model("baseline_classifier")
        return self.pipeline


# Global accessor
def get_model():
    return BaselineClassifier()
