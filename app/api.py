"""
api.py — L6 Production-Ready FastAPI Inference Service

Features:
✔ FastAPI async endpoints
✔ Pydantic request validation
✔ Automatic preprocessing + inference pipeline
✔ Health/liveness/readiness endpoints (Kubernetes-ready)
✔ Logging for observability
✔ Batch & real-time prediction support
✔ Works with Docker, Kubernetes, CI/CD

This API serves your ML model in production.
"""

import logging
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Optional, Union

from pipelines.inference_pipeline import (
    run_realtime_inference,
    run_batch_inference,
)
from utils.config import get_config

logger = logging.getLogger("FastAPI")
logger.setLevel(logging.INFO)

app = FastAPI(
    title="Cautious Enigma ML Inference API",
    description="L6-grade FastAPI server for vehicle safety classification",
    version="1.0.0"
)

cfg = get_config()
EXPECTED_FEATURES = cfg.get("data.features")


# ------------------------------------------------------
# Request Models
# ------------------------------------------------------

class PredictionRequest(BaseModel):
    """Schema for real-time prediction."""
    data: dict = Field(
        ..., example={"speed": 55, "visibility": 0.9, "weather": 2}
    )


class BatchPredictionRequest(BaseModel):
    """Schema for batch prediction over file paths."""
    input_file: str = Field(..., example="data/input.csv")
    output_file: Optional[str] = Field(
        None, example="data/predictions.csv"
    )


# ------------------------------------------------------
# Health Check Endpoints (Kubernetes)
# ------------------------------------------------------

@app.get("/health")
async def health_check():
    """Basic health check."""
    return {"status": "ok"}

@app.get("/live")
async def liveness_probe():
    """K8s liveness probe."""
    return {"alive": True}

@app.get("/ready")
async def readiness_probe():
    """K8s readiness probe."""
    return {"ready": True}


# ------------------------------------------------------
# REAL-TIME PREDICTION ENDPOINT
# ------------------------------------------------------

@app.post("/predict")
async def predict(req: PredictionRequest):
    """
    Real-time model prediction endpoint.

    Example payload:
    {
        "data": {"speed": 60, "visibility": 0.8, "weather": 1}
    }
    """
    logger.info("Received real-time prediction request...")
    try:
        results = run_realtime_inference(req.data)
        return {"prediction": results}
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        return {"error": str(e)}


# ------------------------------------------------------
# BATCH INFERENCE ENDPOINT
# ------------------------------------------------------

@app.post("/batch_predict")
async def batch_predict(req: BatchPredictionRequest):
    """
    Batch prediction endpoint.

    Accepts a CSV or Parquet file path and returns or saves predictions.
    """
    logger.info(
        f"Received batch prediction request "
        f"for => {req.input_file}"
    )

    try:
        results = run_batch_inference(req.input_file, req.output_file)
        return {
            "status": "success",
            "rows_processed": len(results),
            "output_file": req.output_file,
        }
    except Exception as e:
        logger.error(f"Batch inference error: {e}")
        return {"error": str(e)}


# ------------------------------------------------------
# ROOT
# ------------------------------------------------------

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Cautious Enigma ML Inference API",
        "available_endpoints": [
            "/predict",
            "/batch_predict",
            "/health",
            "/ready",
            "/live"
        ]
    }
