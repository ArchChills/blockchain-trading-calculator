def confidence_score(rsi_value, trend):
    score = 0

    if rsi_value < 30:
        score += 30
    elif rsi_value > 70:
        score -= 30

    if trend == "bullish":
        score += 20

    return max(0, min(score, 100))
