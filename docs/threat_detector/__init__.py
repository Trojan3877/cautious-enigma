# threat_detector/__init__.py

"""
Threat Detector Package
Modular ML pipeline for cybersecurity threat detection.
"""

__version__ = "1.0.0"

from .data_loader import preprocess_logs
from .feature_engineering import extract_features
from .model import train_model, load_model
from .detector import detect_threats
from .alert import send_alert
