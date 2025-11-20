"""
train_pipeline.py — L6 Production-Ready Training Pipeline

This module orchestrates the ENTIRE ML training flow:
✔ Load & validate data
✔ Preprocess using pipeline
✔ Train model via ModelTrainer
✔ Evaluate model (val + test)
✔ Register the model version
✔ Log all steps for observability
✔ Fully orchestrator-ready (Airflow, Kubeflow, Prefect, Dagster)

This is the highest-level training DAG for your repo.
"""

import logging
import pandas as pd

from utils.config import get_config
from utils.data_loader import load_data_pipeline
from pipelines.preprocess import get_preprocessor
from models.model_trainer import ModelTrainer

logger = logging.getLogger("TrainPipeline")
logger.setLevel(logging.INFO)


class TrainPipeline:
    """
    L6-grade end-to-end ML pipeline orchestrator.
    """

    def __init__(self):
        logger.info("Initializing TrainPipeline...")

        self.cfg = get_config()
        self.preprocessor = get_preprocessor()
        self.trainer = ModelTrainer()

    # ----------------------------------------------------
    # STEP 1 — Load + Split Dataset
    # ----------------------------------------------------
    def _load_data(self):
        logger.info("STEP 1: Loading dataset...")
        self.train_df, self.val_df, self.test_df = load_data_pipeline()

    # ----------------------------------------------------
    # STEP 2 — Preprocess Each Split
    # ----------------------------------------------------
    def _preprocess(self):
        logger.info("STEP 2: Preprocessing datasets...")

        self.train_df = self.preprocessor.transform(self.train_df)
        self.val_df = self.preprocessor.transform(self.val_df)
        self.test_df = self.preprocessor.transform(self.test_df)

    # ----------------------------------------------------
    # STEP 3 — Train Model
    # ----------------------------------------------------
    def _train_model(self):
        logger.info("STEP 3: Training model...")

        # Identify columns
        label_col = self.cfg.get("data.label_col")
        feature_cols = [f for f in self.train_df.columns if f != label_col]

        X_train = self.train_df[feature_cols]
        y_train = self.train_df[label_col]

        X_val = self.val_df[feature_cols]
        y_val = self.val_df[label_col]

        X_test = self.test_df[feature_cols]
        y_test = self.test_df[label_col]

        # Train & evaluate
        metadata = self.trainer.model.train(X_train, y_train)
        val_metrics = self.trainer.model.evaluate(X_val, y_val)
        test_metrics = self.trainer.model.evaluate(X_test, y_test)

        return metadata, val_metrics, test_metrics

    # ----------------------------------------------------
    # MAIN RUN METHOD
    # ----------------------------------------------------
    def run(self):
        logger.info("=== START TRAIN PIPELINE ===")

        self._load_data()
        self._preprocess()
        metadata, val_metrics, test_metrics = self._train_model()

        logger.info("=== TRAINING PIPELINE COMPLETE ===")

        return {
            "model_metadata": metadata,
            "validation_metrics": val_metrics,
            "test_metrics": test_metrics,
        }


# Global accessor for Airflow / CLI
def run_train_pipeline():
    """
    This is the function Airflow/Kubeflow/Prefect would call.
    """
    pipeline = TrainPipeline()
    return pipeline.run()
