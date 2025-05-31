import streamlit as st
import folium
from streamlit.components.v1 import html

# 여행지 리스트
travel_spots = [
    {"name": "서울", "lat": 37.5665, "lon": 126.9780, "desc": "문화와 역사의 중심지", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Seoul_skyline.jpg"},
    {"name": "부산", "lat": 35.1796, "lon": 129.0756, "desc": "바다와 야경이 아름다운 항구 도시", "img": "https://upload.wikimedia.org/wikipedia/commons/2/26/Busan_night.jpg"},
    {"name": "제주도", "lat": 33.4996, "lon": 126.5312, "desc": "자연과 휴양의 천국", "img": "https://upload.wikimedia.org/wikipedia/commons/3/37/Jeju_seongsan.jpg"},
    {"name": "경주", "lat": 35.8562, "lon": 129.2247, "desc": "천년 고도, 신라의 고도", "img": "https://upload.wikimedia.org/wikipedia/commons/5/53/Bulguksa_Temple.jpg"},
    {"name": "강릉", "lat": 37.7519, "lon": 128.8761, "desc": "동해안의 매력 도시", "img": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Gangneung-beach.jpg"},
    {"name": "인천", "lat": 37.4563, "lon": 126.7052, "desc": "차이나타운과 공항의 도시", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3b/Incheon_Songdo.jpg"},
    {"name": "속초", "lat": 38.2044, "lon": 128.5912, "desc": "설악산과 바다가 어우러진 자연도시", "img": "https://upload.wikimedia.org/wikipedia/commons/f/f7/Sokcho_harbor.jpg"},
    {"name": "전주", "lat": 35.8242, "lon": 127.1480, "desc": "한옥과 한식의 전통 도시", "img": "https://upload.wikimedia.org/wikipedia/commons/7/75/Jeonju_Hanok_Village.jpg"},
    {"name": "여수", "lat": 34.7604, "lon": 127.6622, "desc": "밤바다가 낭만적인 항구 도시", "img": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Yeosu_night.jpg"},
    {"name": "남해", "lat": 34.8372, "lon": 127.8920, "desc": "조용하고 아름다운 힐링 섬", "img": "https://upload.wikimedia.org/wikipedia/commons/2/21/Namhae.jpg"},
]

# 페이지 설정
st.set_page_config(page_title="한국 Top10 여행지", layout="wide")
st.title("💖 한국인이 가장 사랑하는 Top 10 여행지")
st.markdown("아래 지도와 카드에서 각 여행지를 만나보세요!")

# Folium 지도 생성
m = folium.Map(location=[36.5, 127.8], zoom_start=7)

for spot in travel_spots:
    folium.Marker(
        [spot["lat"], spot["lon"]],
        tooltip=spot["name"],
        popup=f"<b>{spot['name']}</b><br>{spot['desc']}",
        icon=folium.Icon(color="pink", icon="heart")
    ).add_to(m)

# 지도 렌더링
html(m._repr_html_(), height=500)

# 카드 스타일 정의
card_css = """
<style>
.card {
    background-color: #fff0f5;
    border-radius: 16px;
    padding: 1rem;
    margin: 1rem 0.5rem;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    text-align: center;
}
.card img {
    border-radius: 12px;
    width: 100%;
    height: 200px;
    object-fit: cover;
}
.card h4 {
    margin: 0.5rem 0 0.2rem;
    color: #d63384;
}
.card p {
    color: #555;
    font-size: 0.95rem;
}
</style>
"""
st.markdown(card_css, unsafe_allow_html=True)

# 여행지 카드 출력 (2열)
cols = st.columns(2)
for i, spot in enumerate(travel_spots):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="card">
            <img src="{spot['img']}">
            <h4>{spot['name']}</h4>
            <p>{spot['desc']}</p>
        </div>
        """, unsafe_allow_html=True)
