# threat_scoring.py

def score_threat(row):
    score = 0
    if row["suspicious_flag"]:
        score += 50
    score += min(row["ip_freq"] * 5, 30)
    score += abs(row["hour"] - 12) * 2  # off-peak hours
    return min(score, 100)

def apply_threat_scores(df):
    df["threat_score"] = df.apply(score_threat, axis=1)
    return df
