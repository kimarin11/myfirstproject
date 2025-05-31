import streamlit as st

st.set_page_config(page_title="이상형 테스트 💘", page_icon="💘", layout="centered")

st.title("💘 이상형 성향 테스트")
st.markdown("선택하면 바로 다음 질문으로 넘어가요!\n당신의 취향에 꼭 맞는 이상형을 찾아드릴게요 💖")

# 상태 초기화
if 'step' not in st.session_state:
    st.session_state.step = 1
    st.session_state.answers = {}

def reset():
    st.session_state.step = 1
    st.session_state.answers = {}

# 질문 리스트
questions = [
    ("고양이상 😼", "강아지상 🐶"),
    ("연상 👨‍💼", "동갑 👨", "연하 🧒"),
    ("다정 💗", "츤데레 🙃"),
    ("무쌍 😌", "속쌍 😉", "유쌍 🥰"),
    ("안경 유 🤓", "안경 무 😎"),
    ("키 큰 👠", "키 작은 👟")
]

# 현재 단계
step = st.session_state.step
total = len(questions)

# 질문 단계
if step <= total:
    q = questions[step - 1]
    options = ["👈 선택해주세요"] + list(q)
    selected = st.selectbox(
        f"### Q{step}. 당신의 취향은?",
        options,
        key=f"select_{step}"
    )

    if selected != "👈 선택해주세요":
        st.session_state.answers[f"Q{step}"] = selected
        st.session_state.step += 1
        st.rerun()

# 결과 단계
else:
    st.success("🎉 테스트 완료!")
    st.toast("당신에게 어울리는 이상형을 찾는 중... 💘", icon="🔍")
    st.snow()

    a = st.session_state.answers

    # 다양한 조건 조합에 따른 결과 (간단 예시)
    if (
        a.get("Q1") == "강아지상 🐶"
        and a.get("Q2") == "연하 🧒"
        and a.get("Q3") == "다정 💗"
    ):
        img = "https://generated.photos/vue-static/home/face-generator/age-male-before.jpg"
        desc = """
        🐶 귀엽고 다정한 연하남  
        ☀️ 항상 에너지 넘치고 장난기 많은 스타일  
        📦 선물보다 마음을 자주 표현하는 타입
        """
    elif (
        a.get("Q1") == "고양이상 😼"
        and a.get("Q2") == "연상 👨‍💼"
        and a.get("Q3") == "츤데레 🙃"
    ):
        img = "https://generated.photos/vue-static/home/face-generator/face2.jpg"
        desc = """
        🖤 차가운 듯 다정한 연상 고양이상  
        💼 말보다 행동으로 표현하는 츤데레  
        ☕ 혼자 있어도 멋진, 묘하게 끌리는 사람
        """
    elif a.get("Q5") == "안경 유 🤓" and a.get("Q4") == "무쌍 😌":
        img = "https://generated.photos/vue-static/home/face-generator/face4.jpg"
        desc = """
        📚 문학 감성의 지적인 이상형  
        🎧 조용한 곳에서 음악 들으며 산책하는 걸 좋아해요  
        😌 시선은 차분하지만 마음은 따뜻한 사람
        """
    else:
        img = "https://generated.photos/vue-static/home/face-generator/face3.jpg"
        desc = """
        🎮 장난도 잘 치고 분위기 메이커  
        😄 대화가 끊기지 않고 항상 웃게 되는 스타일  
        🎧 "같이 있으면 시간 순삭!" 같은 에너지 넘치는 사람
        """

    st.markdown("## 💘 당신에게 어울리는 이상형은 이런 느낌!")
    st.image(img, width=240, caption="✨ 이상형 이미지 (AI 생성)")
    st.markdown(desc)
    st.balloons()

    if st.button("🔄 다시 하기"):
        reset()
