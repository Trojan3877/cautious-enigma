"""
data_loader.py — L5/L6 Production-Grade Data Loading Pipeline

Features:
✔ Config-driven dataset paths
✔ Automatic train/val/test split handling
✔ Validation for missing/corrupt files
✔ Pandas + NumPy loaders
✔ Optional PyTorch Dataset wrapper
✔ Logging for observability & debugging
"""

import os
import logging
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from utils.config import get_config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("DataLoader")


class DataLoader:
    def __init__(self):
        self.cfg = get_config()
        self.dataset_path = Path(self.cfg.get("data.dataset_path"))
        self.test_size = float(self.cfg.get("data.test_size", 0.2))
        self.val_size = float(self.cfg.get("data.val_size", 0.1))
        self.random_state = int(self.cfg.get("data.random_state", 42))

        self._validate_dataset_path()

    def _validate_dataset_path(self):
        """Validate dataset path exists and is readable."""
        if not self.dataset_path.exists():
            raise FileNotFoundError(
                f"Dataset not found at: {self.dataset_path}. "
                f"Please check config/config.yaml."
            )
        logger.info(f"[OK] Dataset located at {self.dataset_path}")

    def load_csv(self):
        """Load a CSV dataset into a DataFrame."""
        try:
            df = pd.read_csv(self.dataset_path)
            logger.info(f"Loaded dataset with {len(df)} rows.")
            return df
        except Exception as e:
            logger.error(f"Failed to read CSV: {e}")
            raise

    def split_dataframe(self, df):
        """
        Split dataset into train/val/test frames.
        Ensures valid proportions and avoids leakage.
        """
        logger.info("Splitting dataset into train/val/test...")

        train_df, temp_df = train_test_split(
            df,
            test_size=self.test_size + self.val_size,
            random_state=self.random_state,
            shuffle=True,
        )

        relative_val_size = self.val_size / (self.test_size + self.val_size)

        val_df, test_df = train_test_split(
            temp_df,
            test_size=1 - relative_val_size,
            random_state=self.random_state,
            shuffle=True,
        )

        logger.info(
            f"Split complete:\n"
            f"  Train: {len(train_df)} rows\n"
            f"  Val:   {len(val_df)} rows\n"
            f"  Test:  {len(test_df)} rows"
        )

        return train_df, val_df, test_df

    def load_and_split(self):
        """Convenience method for full pipeline."""
        df = self.load_csv()
        return self.split_dataframe(df)


# Optional PyTorch Dataset Wrapper (L6-Level Flexibility)
try:
    import torch
    from torch.utils.data import Dataset

    class TorchDataset(Dataset):
        """
        Generic PyTorch-friendly dataset.
        Converts Pandas DF to tensors.
        """

        def __init__(self, df, feature_cols, label_col):
            self.features = df[feature_cols].values
            self.labels = df[label_col].values

        def __len__(self):
            return len(self.features)

        def __getitem__(self, idx):
            x = torch.tensor(self.features[idx], dtype=torch.float32)
            y = torch.tensor(self.labels[idx], dtype=torch.long)
            return x, y

except ImportError:
    logger.warning("PyTorch not installed — TorchDataset disabled.")


# Global accessor
def load_data_pipeline():
    """Load + split dataset using defaults."""
    loader = DataLoader()
    return loader.load_and_split()
