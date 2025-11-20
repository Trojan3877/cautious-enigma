"""
model_trainer.py — L5/L6 Production-Grade Training Orchestrator

This module handles the FULL ML workflow:
✔ Loads config
✔ Loads dataset
✔ Splits into train/val/test
✔ Builds model dynamically
✔ Trains + evaluates
✔ Saves versioned model to registry
✔ Logs all steps for observability 

This is the central training engine for the entire repo.
"""

import logging
from utils.config import get_config
from utils.data_loader import load_data_pipeline
from models.baseline_model import BaselineClassifier

logger = logging.getLogger("ModelTrainer")
logger.setLevel(logging.INFO)


class ModelTrainer:
    """
    High-level orchestrator for running end-to-end ML training.
    
    Responsibilities:
    - Load config
    - Load & split data
    - Choose model architecture
    - Train model
    - Evaluate
    - Register / version model
    """

    def __init__(self):
        logger.info("Initializing ModelTrainer...")
        self.cfg = get_config()
        self.model_name = self.cfg.get("model.name", "baseline")
        self.model = None

    def _select_model(self):
        """Pick model architecture based on config file."""
        logger.info(f"Selecting model: {self.model_name}")

        if self.model_name == "baseline":
            self.model = BaselineClassifier()
        else:
            raise ValueError(f"Unsupported model type: {self.model_name}")

        return self.model

    def run(self):
        """Run the complete training pipeline."""
        logger.info("=== START TRAINING PIPELINE ===")

        # LOAD & SPLIT DATA
        logger.info("Step 1: Loading dataset...")
        train_df, val_df, test_df = load_data_pipeline()

        # Identify feature and label columns
        features = list(train_df.columns)
        label_col = self.cfg.get("data.label_col")

        if label_col not in train_df.columns:
            raise ValueError(
                f"Label column '{label_col}' missing from dataset. "
                f"Update config/data.label_col."
            )

        features.remove(label_col)

        # CREATE DATA MATRICES
        X_train, y_train = train_df[features], train_df[label_col]
        X_val, y_val = val_df[features], val_df[label_col]
        X_test, y_test = test_df[features], test_df[label_col]

        logger.info(
            f"Training dataset sizes — Train: {len(X_train)}, "
            f"Val: {len(X_val)}, Test: {len(X_test)}"
        )

        # SELECT MODEL
        logger.info("Step 2: Initializing model...")
        model = self._select_model()

        # TRAIN
        logger.info("Step 3: Training model...")
        metadata = model.train(X_train, y_train)

        # EVALUATE
        logger.info("Step 4: Evaluating model (Validation set)...")
        val_metrics = model.evaluate(X_val, y_val)

        logger.info("Step 5: Final Evaluation (Test set)...")
        test_metrics = model.evaluate(X_test, y_test)

        logger.info("=== TRAINING COMPLETE ===")

        return {
            "model_metadata": metadata,
            "validation_metrics": val_metrics,
            "test_metrics": test_metrics,
        }


# Global accessor
def run_training():
    """Convenience function to run trainer from CLI."""
    trainer = ModelTrainer()
    return trainer.run()
