# api.py

from flask import Flask, request, jsonify
from data_loader import preprocess_logs
from feature_engineering import extract_features
from detector import detect_threats

app = Flask(__name__)

@app.route("/detect", methods=["POST"])
def detect():
    try:
        data = request.get_json()
        df = preprocess_logs(pd.DataFrame(data))
        features = extract_features(df)
        threats = detect_threats(features)
        return jsonify({"threat_indices": threats}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


# Run the API
python api.py

# Example POST request
curl -X POST http://localhost:5000/detect \
     -H "Content-Type: application/json" \
     -d '[{"timestamp":"2025-09-28T12:00:00","source_ip":"192.168.1.1","message":"unauthorized access"}]'
