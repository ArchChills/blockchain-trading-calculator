def parse_rupiah(text):
    try:
        return int(text.replace(".", "").replace(",", "").strip())
    except:
        return 0

def format_rupiah(angka):
    return f"Rp {angka:,.0f}".replace(",", ".")
