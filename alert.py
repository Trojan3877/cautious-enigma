# alert.py

import logging
import requests
from config import ALERT_EMAIL, ALERT_WEBHOOK_URL, LOG_LEVEL

logging.basicConfig(level=LOG_LEVEL)

def send_console_alert(threat_indices):
    if not threat_indices:
        logging.info("No threats to alert.")
        return
    logging.warning(f"Threats detected at indices: {threat_indices}")

def send_webhook_alert(threat_indices):
    if not threat_indices:
        return
    payload = {
        "alert": "Threats detected",
        "indices": threat_indices
    }
    try:
        response = requests.post(ALERT_WEBHOOK_URL, json=payload)
        if response.status_code == 200:
            logging.info("Webhook alert sent successfully.")
        else:
            logging.error(f"Webhook alert failed: {response.status_code}")
    except Exception as e:
        logging.error(f"Error sending webhook alert: {e}")
