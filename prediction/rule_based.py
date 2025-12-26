def market_trend(price, sma):
    if sma is None:
        return "unknown"
    if price > sma:
        return "bullish"
    elif price < sma:
        return "bearish"
    return "sideways"


def confidence_score(rsi_value, trend):
    score = 50  # netral

    if rsi_value is not None:
        if rsi_value < 30:
            score += 20
        elif rsi_value > 70:
            score -= 20

    if trend == "bullish":
        score += 15
    elif trend == "bearish":
        score -= 15

    return max(0, min(score, 100))
