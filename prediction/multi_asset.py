from data.price_source import get_price_history
from prediction.indicators import simple_moving_average, rsi
from prediction.rule_based import market_trend, confidence_score

def analyze_asset(coin_id, days=30):
    prices = get_price_history(coin_id, days)

    current = prices[-1]
    sma = simple_moving_average(prices)
    rsi_val = rsi(prices)

    trend = market_trend(current, sma)
    confidence = confidence_score(rsi_val, trend)

    return {
        "price": current,
        "trend": trend,
        "rsi": rsi_val,
        "confidence": confidence,
    }
