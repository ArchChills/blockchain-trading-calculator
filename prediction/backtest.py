def backtest_simple(prices, buy_rsi=30, sell_rsi=70):
    balance = 100
    position = False
    trades = 0

    for i in range(14, len(prices)):
        rsi_now = prices[i] - prices[i-1]

        if not position and rsi_now < buy_rsi:
            position = True
            entry = prices[i]
            trades += 1

        elif position and rsi_now > sell_rsi:
            balance *= prices[i] / entry
            position = False

    return {
        "final_balance": round(balance, 2),
        "profit_pct": round((balance - 100), 2),
        "trades": trades,
    }
