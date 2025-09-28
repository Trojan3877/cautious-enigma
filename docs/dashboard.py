# dashboard.py

from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px
from data_loader import preprocess_logs
from feature_engineering import extract_features
from detector import detect_threats

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    threat_indices = []
    fig_html = None

    if request.method == "POST":
        uploaded_file = request.files["logfile"]
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
            df = preprocess_logs(df)
            features = extract_features(df)
            threat_indices = detect_threats(features)

            df["threat"] = 0
            for i in threat_indices:
                df.loc[i, "threat"] = 1

            fig = px.scatter(df, x="hour", y="ip_freq", color="threat", title="Threat Detection")
            fig_html = fig.to_html(full_html=False)

    return render_template("dashboard.html", fig_html=fig_html, threat_indices=threat_indices)

if __name__ == "__main__":
    app.run(debug=True)
