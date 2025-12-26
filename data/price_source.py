import requests
import streamlit as st

@st.cache_data(ttl=300)  # cache 5 menit
def get_price_history(coin_id, days=30):
    url = (
        f"https://api.coingecko.com/api/v3/coins/"
        f"{coin_id}/market_chart"
        f"?vs_currency=usd&days={days}"
    )

    response = requests.get(url, timeout=10)
    data = response.json()

    if "prices" not in data:
        raise ValueError(
            f"API limit / error untuk '{coin_id}'. "
            f"Coba beberapa menit lagi."
        )

    return [p[1] for p in data["prices"]]
