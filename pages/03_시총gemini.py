import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta

# 페이지 설정
st.set_page_config(page_title="시가총액 Top10 추이", layout="wide")
st.title("🌎 전 세계 시가총액 Top 10 기업의 최근 3년 시가총액 변화")

# 기업 티커 및 이름 매핑
companies = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Alphabet (Google)": "GOOG",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Meta": "META",
    "Tesla": "TSLA",
    "Berkshire Hathaway": "BRK-B",
    "TSMC": "TSM",
    # "Saudi Aramco": "2222.SR",  # Yahoo Finance API에서 제한 있음
}

# 기간 설정
end_date = datetime.today()
start_date = end_date - timedelta(days=3 * 365)

# 데이터 가져오기
@st.cache_data
def load_market_caps():
    df_caps = pd.DataFrame()
    for name, ticker in companies.items():
        data = yf.Ticker(ticker).history(start=start_date, end=end_date, interval="1mo")
        data["MarketCap"] = data["Close"] * yf.Ticker(ticker).info.get("sharesOutstanding", 0)
        data = data[["MarketCap"]].rename(columns={"MarketCap": name})
        if df_caps.empty:
            df_caps = data
        else:
            df_caps = df_caps.join(data, how="outer")
    df_caps.index = df_caps.index.strftime("%Y-%m")  # 월 단위 포맷
    return df_caps.fillna(method="ffill")

df_caps = load_market_caps()

# Plotly 그래프
fig = go.Figure()
for company in companies:
    fig.add_trace(go.Scatter(
        x=df_caps.index,
        y=df_caps[company] / 1e9,  # 단위: 십억 달러
        mode='lines+markers',
        name=company
    ))

fig.update_layout(
    title="최근 3년간 시가총액 추이 (단위: 십억 달러)",
    xaxis_title="날짜",
    yaxis_title="시가총액 (Billion USD)",
    hovermode="x unified",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)
