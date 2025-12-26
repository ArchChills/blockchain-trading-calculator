def simple_moving_average(data, period=14):
    if len(data) < period:
        return None
    return sum(data[-period:]) / period


def rsi(data, period=14):
    if len(data) < period + 1:
        return None

    gains, losses = 0, 0
    for i in range(-period, -1):
        diff = data[i + 1] - data[i]
        if diff > 0:
            gains += diff
        else:
            losses -= diff

    if losses == 0:
        return 100

    rs = gains / losses
    return 100 - (100 / (1 + rs))
