import streamlit as st
from services.calculator import hitung_trading_btc,format_rupiah, parse_rupiah

st.set_page_config(page_title="Bitcoin Trading Calculator", layout="centered")

st.title("📊 Bitcoin Trading Calculator (NON-AI)")

st.sidebar.header("Input Trading")

harga_beli_text = st.sidebar.text_input(
    "Harga Beli Bitcoin (Rp)",
    value="900.000.000"
)

modal_text = st.sidebar.text_input(
    "Modal (Rp)",
    value="10.000.000"
)

target_jual_text = st.sidebar.text_input(
    "Target Jual Bitcoin (Rp)",
    value="990.000.000"
)

stop_loss_text = st.sidebar.text_input(
    "Stop Loss Bitcoin (Rp)",
    value="870.000.000"
)

if st.sidebar.button("Hitung Trading"):
    harga_beli = parse_rupiah(harga_beli_text)
    modal = parse_rupiah(modal_text)
    target_jual = parse_rupiah(target_jual_text)
    stop_loss = parse_rupiah(stop_loss_text)
    
    hasil = hitung_trading_btc(
        harga_beli, modal, target_jual, stop_loss
    )

    st.subheader("📌 Posisi Trading")

    st.write(f"Jumlah BTC dibeli: **{hasil['jumlah_btc']:.6f} BTC**")

    st.divider()
    st.subheader("💰 Profit (Reward)")

    st.metric(
        "Keuntungan",
        format_rupiah(hasil["keuntungan"]),
        f"{hasil['keuntungan_persen']:.2f}%"
    )

    st.metric(
        "Kerugian Maksimal",
        format_rupiah(hasil["risiko"]),
        f"-{hasil['risiko_persen']:.2f}%"
    )

    st.divider()
    st.subheader("⚠️ Risiko (Stop Loss)")

    st.metric(
        "Kerugian Maksimal",
        f"Rp {hasil['risiko']:,.0f}",
        f"-{hasil['risiko_persen']:.2f}%"
    )

    st.write(
        f"Penurunan harga ke stop loss: "
        f"**{hasil['price_change_stop']:.2f}%**"
    )

    st.divider()
    st.subheader("📐 Risk–Reward Ratio")

    st.write(f"RRR = **1 : {hasil['rrr']:.2f}**")

    if hasil["rrr"] >= 2:
        st.success("Risk–Reward BAGUS (≥ 1:2)")
    elif hasil["rrr"] >= 1:
        st.warning("Risk–Reward CUKUP (1:1)")
    else:
        st.error("Risk–Reward BURUK (< 1:1)")
