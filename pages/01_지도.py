import streamlit as st
import folium
from streamlit.components.v1 import html

# 여행지 정보
travel_spots = [
    {"name": "서울", "lat": 37.5665, "lon": 126.9780, "desc": "문화와 역사의 중심지", "image": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Seoul_skyline.jpg"},
    {"name": "부산", "lat": 35.1796, "lon": 129.0756, "desc": "해운대, 광안리의 활기찬 항구도시", "image": "https://upload.wikimedia.org/wikipedia/commons/2/26/Busan_night.jpg"},
    {"name": "제주도", "lat": 33.4996, "lon": 126.5312, "desc": "화산섬의 자연과 휴양의 천국", "image": "https://upload.wikimedia.org/wikipedia/commons/3/37/Jeju_seongsan.jpg"},
    {"name": "경주", "lat": 35.8562, "lon": 129.2247, "desc": "천년 고도, 신라의 역사도시", "image": "https://upload.wikimedia.org/wikipedia/commons/5/53/Bulguksa_Temple.jpg"},
    {"name": "강릉", "lat": 37.7519, "lon": 128.8761, "desc": "커피향 가득한 동해 해변 도시", "image": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Gangneung-beach.jpg"},
    {"name": "인천", "lat": 37.4563, "lon": 126.7052, "desc": "공항과 차이나타운, 송도의 도시", "image": "https://upload.wikimedia.org/wikipedia/commons/3/3b/Incheon_Songdo.jpg"},
    {"name": "속초", "lat": 38.2044, "lon": 128.5912, "desc": "설악산과 바다가 만나는 곳", "image": "https://upload.wikimedia.org/wikipedia/commons/f/f7/Sokcho_harbor.jpg"},
    {"name": "전주", "lat": 35.8242, "lon": 127.1480, "desc": "한옥과 한식의 고장", "image": "https://upload.wikimedia.org/wikipedia/commons/7/75/Jeonju_Hanok_Village.jpg"},
    {"name": "여수", "lat": 34.7604, "lon": 127.6622, "desc": "낭만의 밤바다", "image": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Yeosu_night.jpg"},
    {"name": "남해", "lat": 34.8372, "lon": 127.8920, "desc": "힐링과 자연의 섬", "image": "https://upload.wikimedia.org/wikipedia/commons/2/21/Namhae.jpg"},
]

st.set_page_config(page_title="한국 Top10 여행지", layout="wide")
st.title("🇰🇷 한국인이 가장 사랑하는 Top 10 여행지")
st.markdown("지도에서 위치를 확인하고 아래에서 사진과 함께 여행지를 살펴보세요!")

# 지도 생성
m = folium.Map(location=[36.5, 127.8], zoom_start=7)
for spot in travel_spots:
    folium.Marker(
        location=[spot["lat"], spot["lon"]],
        popup=f"<b>{spot['name']}</b><br>{spot['desc']}",
        tooltip=spot["name"],
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# 지도 렌더링
map_html = m._repr_html_()
html(map_html, height=500)

# 카드 스타일
card_style = """
<style>
.card {
    background-color: #fff0f5;
    border-radius: 15px;
    padding: 1rem;
    margin: 1rem 0.5rem;
    box-shadow: 2px 2px 12px rgba(0,0,0,0.1);
}
.card img {
    border-radius: 10px;
    width: 100%;
    height: 200px;
    object-fit: cover;
}
.card h4 {
    margin-top: 0.5rem;
    color: #cc3366;
}
</style>
"""
st.markdown(card_style, unsafe_allow_html=True)

# 2열 그리드로 여행지 카드 표시
cols = st.columns(2)
for i, spot in enumerate(travel_spots):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="card">
            <img src="{spot['image']}">
            <h4>{spot['name']}</h4>
            <p>{spot['desc']}</p>
        </div>
        """, unsafe_allow_html=True)
