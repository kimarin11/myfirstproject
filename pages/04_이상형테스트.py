import streamlit as st

st.set_page_config(page_title="이상형 테스트 💘", page_icon="💘", layout="centered")

st.title("💘 나의 이상형 찾기 테스트")
st.markdown("선택만 하면 바로 넘어가는 자동 진행 테스트예요! 😍")

# 세션 초기화
if "step" not in st.session_state:
    st.session_state.step = 1
    st.session_state.answers = {}

def next_step():
    st.session_state.step += 1

# 질문 리스트
questions = [
    ("고양이상 😼", "강아지상 🐶"),
    ("연상 👨‍💼", "동갑 👨", "연하 🧒"),
    ("다정 💗", "츤데레 🙃"),
    ("무쌍 😌", "속쌍 😉", "유쌍 🥰"),
    ("안경 유 🤓", "안경 무 😎"),
    ("키 큰 👠", "키 작은 👟")
]

step = st.session_state.step
total = len(questions)

if step <= total:
    q = questions[step - 1]
    st.markdown(f"### Q{step}. 당신의 취향은?")
    
    choice = st.radio("👇 선택하세요", q, key=f"q{step}", on_change=next_step)
    st.session_state.answers[f"Q{step}"] = choice

else:
    st.success("🎉 테스트 완료!")
    st.balloons()

    a = st.session_state.answers

    # 기본값
    img = "https://generated.photos/vue-static/home/face-generator/face3.jpg"
    desc = "🎮 장난도 잘 치고 분위기 메이커\n😄 대화가 끊기지 않고 항상 웃게 되는 스타일\n🎧 '같이 있으면 시간 순삭!' 같은 에너지 넘치는 사람"

    # 커스텀 조건 예시 (더 추가 가능)
    if (
        a.get("Q1") == "강아지상 🐶"
        and a.get("Q2") == "연하 🧒"
        and a.get("Q3") == "다정 💗"
    ):
        img = "https://generated.photos/vue-static/home/face-generator/age-male-before.jpg"
        desc = "🐶 귀엽고 다정한 연하남\n🍬 언제나 붙어있고 싶게 만드는 애교 많은 스타일\n💬 하루 종일 연락해도 지루하지 않아요!"
    elif (
        a.get("Q1") == "고양이상 😼"
        and a.get("Q2") == "연상 👨‍💼"
        and a.get("Q3") == "츤데레 🙃"
    ):
        img = "https://generated.photos/vue-static/home/face-generator/face2.jpg"
        desc = "🖤 첫인상은 시크하지만 알고 보면 따뜻한 츤데레\n☕ 조용한 데이트를 즐기고, 말보단 행동으로 표현해요\n📚 독서와 클래식을 좋아하는 스마트한 남자"
    elif a.get("Q5") == "안경 유 🤓" and a.get("Q4") == "무쌍 😌":
        img = "https://generated.photos/vue-static/home/face-generator/face4.jpg"
        desc = "📘 지적이고 차분한 분위기의 무쌍 안경남\n🎧 인디 음악 듣고 혼자 영화 보는 걸 좋아해요\n👓 무심한 듯 챙겨주는 말에 심쿵!"
    elif a.get("Q6") == "키 큰 👠" and a.get("Q3") == "다정 💗":
        img = "https://generated.photos/vue-static/home/face-generator/face5.jpg"
        desc = "🧸 키 크고 믿음직한 다정남\n🙌 포옹 하나로 모든 걱정을 날려주는 사람\n🍰 카페에서 부드러운 디저트를 같이 나눠 먹는 타입"

    # 결과 출력
    st.markdown("## 💘 당신에게 어울리는 이상형은 이런 사람!")
    st.image(img, caption="✨ AI로 생성된 이상형 이미지", width=250)
    st.markdown(desc)

    if st.button("🔁 다시 하기"):
        st.session_state.step = 1
        st.session_state.answers = {}
