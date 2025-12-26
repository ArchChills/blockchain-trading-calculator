def hitung_trading_btc(harga_beli, modal, target_jual, stop_loss):
    jumlah_btc = modal / harga_beli

    nilai_jual = jumlah_btc * target_jual
    keuntungan = nilai_jual - modal
    keuntungan_persen = (keuntungan / modal) * 100

    nilai_stop = jumlah_btc * stop_loss
    risiko = modal - nilai_stop
    risiko_persen = (risiko / modal) * 100

    price_change_target = ((target_jual - harga_beli) / harga_beli) * 100
    price_change_stop = ((harga_beli - stop_loss) / harga_beli) * 100

    risk_reward_ratio = keuntungan / risiko if risiko > 0 else 0

    return {
        "jumlah_btc": jumlah_btc,
        "keuntungan": keuntungan,
        "keuntungan_persen": keuntungan_persen,
        "risiko": risiko,
        "risiko_persen": risiko_persen,
        "price_change_target": price_change_target,
        "price_change_stop": price_change_stop,
        "rrr": risk_reward_ratio
    }

def format_rupiah(angka):
    return f"Rp {angka:,.0f}".replace(",", ".")

def parse_rupiah(text):
    """
    Mengubah '900.000.000' -> 900000000
    Aman untuk input user
    """
    try:
        return int(text.replace(".", "").replace(",", "").strip())
    except:
        return 0
