import streamlit as st

# ===== IMPORT CORE MODULES =====
from core.formatter import parse_rupiah, format_rupiah
from core.calculator import calculate_trade
from core.risk import risk_level

# ===== PAGE CONFIG =====
st.set_page_config(
    page_title="Crypto Trading Calculator",
    page_icon="📈",
    layout="centered"
)

# ===== HEADER =====
st.title("📈 Crypto Trading Calculator")
st.caption("Level 1–2 Trading Analytics Tool (Non-AI)")
st.markdown(
    "> Educational & analytical purposes only. Not financial advice."
)

st.divider()

# ===== SIDEBAR INPUT =====
st.sidebar.header("📥 Input Trading")

asset = st.sidebar.selectbox(
    "Pilih Aset Crypto",
    ["Bitcoin (BTC)", "Ethereum (ETH)", "Solana (SOL)", "Custom"]
)

harga_beli_text = st.sidebar.text_input(
    "Harga Beli (Rp)",
    value="900.000.000"
)

modal_text = st.sidebar.text_input(
    "Modal (Rp)",
    value="10.000.000"
)

target_jual_text = st.sidebar.text_input(
    "Target Jual (Rp)",
    value="990.000.000"
)

st.sidebar.info("Stop loss otomatis ditetapkan sebesar 5% dari harga beli.")

# ===== PARSE INPUT =====
harga_beli = parse_rupiah(harga_beli_text)
modal = parse_rupiah(modal_text)
target_jual = parse_rupiah(target_jual_text)

# ===== VALIDATION =====
if harga_beli <= 0 or modal <= 0:
    st.error("Harga beli dan modal harus lebih dari 0.")
    st.stop()

if target_jual <= harga_beli:
    st.warning("Target jual seharusnya lebih tinggi dari harga beli.")

# ===== CALCULATION =====
hasil = calculate_trade(
    harga_beli=harga_beli,
    target_jual=target_jual,
    modal=modal
)

risk_label = risk_level(hasil["rr"])

# ===== OUTPUT =====
st.subheader("📊 Hasil Perhitungan")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="💰 Potensi Keuntungan",
        value=format_rupiah(hasil["profit"]),
        delta=f"{hasil['profit_pct']:.2f}%"
    )

with col2:
    st.metric(
        label="🛑 Stop Loss (5%)",
        value=format_rupiah(hasil["stop_loss"]),
        delta=f"-{hasil['loss_pct']:.0f}%"
    )

st.divider()

col3, col4 = st.columns(2)

with col3:
    st.metric(
        label="⚖️ Risk / Reward Ratio",
        value=f"{hasil['rr']:.2f}"
    )

with col4:
    st.metric(
        label="📉 Risk Level",
        value=risk_label
    )

# ===== TRADE SUMMARY =====
st.subheader("📝 Ringkasan Trading")

st.markdown(
    f"""
    **Aset:** {asset}  
    **Harga Beli:** {format_rupiah(harga_beli)}  
    **Target Jual:** {format_rupiah(target_jual)}  
    **Stop Loss Otomatis (5%):** {format_rupiah(hasil["stop_loss"])}
    **Modal:** {format_rupiah(modal)}  
    """
)

# ===== LEVEL 2 PLACEHOLDER =====
st.divider()
st.subheader("🔮 Prediction (Level 2 – Coming Soon)")

st.info(
    "Prediction module akan menampilkan trend, confidence score, dan "
    "indikator teknikal sederhana (RSI, MA, dll)."
)

# ===== FOOTER =====
st.divider()
st.caption("© 2025 Crypto Trading Analytics Tool | Built with Streamlit")
