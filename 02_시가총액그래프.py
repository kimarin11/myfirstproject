import streamlit as st
import plotly.graph_objs as go
import pandas as pd

# 페이지 설정
st.set_page_config(page_title="Top 10 시가총액 기업 변화", layout="wide")
st.title("🌎 전 세계 시가총액 Top 10 기업 (최근 3년)")

# 샘플 데이터 (실제 시가총액 데이터를 대체해주세요)
data = {
    "Year": ["2022", "2023", "2024"],
    "Apple": [2800, 2600, 2900],
    "Microsoft": [2400, 2500, 2700],
    "Saudi Aramco": [2200, 2100, 2000],
    "Alphabet": [1800, 1700, 1900],
    "Amazon": [1600, 1500, 1800],
    "Nvidia": [700, 1000, 2200],
    "Meta": [900, 800, 1100],
    "Berkshire Hathaway": [600, 700, 750],
    "Tesla": [1000, 900, 850],
    "TSMC": [500, 550, 600]
}

# 데이터프레임 변환
df = pd.DataFrame(data)

# Plotly 그래프 그리기
fig = go.Figure()
for company in df.columns[1:]:
    fig.add_trace(go.Scatter(
        x=df["Year"], y=df[company], mode="lines+markers", name=company
    ))

fig.update_layout(
    title="Top 10 글로벌 기업 시가총액 추이 (단위: 억 달러)",
    xaxis_title="연도",
    yaxis_title="시가총액 (억 달러)",
    hovermode="x unified",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)
