"""
logger.py — Centralized Logging Utility
L5/L6 Production-Grade Logging (Loguru-Based)
"""

from loguru import logger
import sys
from pathlib import Path

# Create log directory if not exists
LOG_DIR = Path("logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE_PATH = LOG_DIR / "app.log"

# Remove default logger to configure custom settings
logger.remove()

# Console logging
logger.add(
    sys.stdout,
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level}</level> | "
           "<cyan>{module}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> — "
           "<level>{message}</level>",
)

# File logging
logger.add(
    LOG_FILE_PATH,
    rotation="10 MB",
    retention="14 days",
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {module}:{function}:{line} — {message}",
)

def get_logger():
    """
    Returns a fully configured Loguru logger.
    Use this in any module that needs logging.
    """
    return logger
