# --- utils/eco_score.py ---
def calculate_eco_score(df):
    target = 100  # hypothetical ideal usage per hour
    df["score"] = 100 - abs(df["water_usage"] - target) / target * 100
    avg_score = max(min(df["score"].mean(), 100), 0)
    return round(avg_score, 2)