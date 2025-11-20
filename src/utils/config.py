"""
config.py — Centralized Configuration Loader
L5/L6 Production-Grade Config System (YAML + Env Overrides)
"""

import os
import yaml
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()  # Load .env file for environment overrides

CONFIG_PATH = Path("config/config.yaml")


class Config:
    """
    Config loader supporting:
    - YAML configuration as the primary source
    - Environment variable overrides
    - Safe defaults for missing keys
    """

    def __init__(self):
        self.raw = self._load_yaml_config()
        self.config = self._apply_env_overrides(self.raw)

    @staticmethod
    def _load_yaml_config():
        """Load config/config.yaml safely."""
        if not CONFIG_PATH.exists():
            raise FileNotFoundError(
                f"Missing config file at {CONFIG_PATH}. "
                "Create one using the template in README."
            )
        with open(CONFIG_PATH, "r") as f:
            return yaml.safe_load(f)

    @staticmethod
    def _apply_env_overrides(config):
        """
        Any key in the YAML config can be overridden
        by an environment variable using uppercase + underscores.
        Example:
            YAML: api.key
            ENV: API_KEY
        """
        def override(obj, prefix=""):
            updated = {}
            for key, value in obj.items():
                env_key = f"{prefix}{key}".upper().replace(".", "_")

                if isinstance(value, dict):
                    updated[key] = override(value, prefix=f"{env_key}_")
                else:
                    updated[key] = os.getenv(env_key, value)
            return updated

        return override(config)

    def get(self, key, default=None):
        """
        Retrieve nested keys using dot notation.
        Ex: config.get("model.learning_rate")
        """
        keys = key.split(".")
        value = self.config

        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value


# Global accessor
_config_instance = None


def get_config():
    """Global entrypoint to load and access configuration."""
    global _config_instance
    if _config_instance is None:
        _config_instance = Config()
    return _config_instance
