def calculate_trade(harga_beli, target_jual, modal, stop_loss_pct=5):
    """
    stop_loss_pct: persen stop loss otomatis (default 5%)
    """

    # Hitung stop loss otomatis
    stop_loss = harga_beli * (1 - stop_loss_pct / 100)

    qty = modal / harga_beli

    profit = (target_jual - harga_beli) * qty
    loss = (harga_beli - stop_loss) * qty

    profit_pct = (target_jual - harga_beli) / harga_beli * 100
    loss_pct = stop_loss_pct

    rr = profit / loss if loss > 0 else 0

    return {
        "stop_loss": stop_loss,
        "profit": profit,
        "loss": loss,
        "profit_pct": profit_pct,
        "loss_pct": loss_pct,
        "rr": rr
    }
