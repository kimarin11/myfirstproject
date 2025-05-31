import streamlit as st

st.set_page_config(page_title="이상형 테스트 💘", page_icon="💘", layout="centered")

st.title("💘 이상형 성향 테스트")
st.markdown("선택만 하면 자동으로 다음 질문으로 넘어가요!\n가장 이상적인 남성상을 찾아드릴게요 💖")

# 초기화
if 'step' not in st.session_state:
    st.session_state.step = 1
    st.session_state.answers = {}

# 질문 정의
questions = [
    ("고양이상 😼", "강아지상 🐶"),
    ("연상 👨‍💼", "동갑 👨", "연하 🧒"),
    ("다정 💗", "츤데레 🙃"),
    ("무쌍 😌", "속쌍 😉", "유쌍 🥰"),
    ("안경 유 🤓", "안경 무 😎"),
    ("키 큰 👠", "키 작은 👟")
]

def on_select_change():
    selected = st.session_state[f"select_{st.session_state.step}"]
    st.session_state.answers[f"Q{st.session_state.step}"] = selected
    st.session_state.step += 1

def reset():
    st.session_state.step = 1
    st.session_state.answers = {}

# 단계별 질문
step = st.session_state.step
total = len(questions)

if step <= total:
    q = questions[step - 1]
    st.markdown(f"### Q{step}. 당신의 취향은?")
    st.selectbox(
        "👇 선택하세요",
        options=q,
        key=f"select_{step}",
        on_change=on_select_change
    )
else:
    st.success("🎉 테스트 완료!")
    st.toast("당신에게 어울리는 이상형을 찾는 중... 💘", icon="🔍")
    st.snow()

    a = st.session_state.answers

    # AI 생성 얼굴 이미지 링크 (픽션 기반, 공개 라이선스 사용 가능)
    # 사용된 얼굴은 실제 인물이 아니며, 캐릭터 표현용
    if (
        a.get("Q1") == "강아지상 🐶"
        and a.get("Q2") == "연하 🧒"
        and a.get("Q3") == "다정 💗"
    ):
        img = "https://generated.photos/vue-static/home/face-generator/age-male-before.jpg"
        desc = """
        🐶 귀엽고 따뜻한 분위기의 연하남  
        🤓 장난기 있지만 누구보다 다정하고 배려심 있는 타입  
        📚 가끔 책 읽다가 자는 모습이 은근히 설레요
        """
    elif (
        a.get("Q1") == "고양이상 😼"
        and a.get("Q2") == "연상 👨‍💼"
        and a.get("Q3") == "츤데레 🙃"
    ):
        img = "https://generated.photos/vue-static/home/face-generator/face2.jpg"
        desc = """
        🖤 시크한 첫인상, 차분한 말투  
        🙃 말보다 행동으로 표현하는 츤데레형  
        ☕ 차 마시며 조용히 같이 있어주는 어른스러운 이상형
        """
    else:
        img = "https://generated.photos/vue-static/home/face-generator/face3.jpg"
        desc = """
        🎮 장난도 잘 치고
