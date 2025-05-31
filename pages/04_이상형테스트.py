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
        st.experimental_rerun()

# 결과 단계
else:
    st.success("🎉 테스트 완료!")
    st.toast("당신에게 어울리는 이상형을 찾는 중... 💘", icon="🔍")
    st.snow()

    a = st.session_state.answers
    desc = ""
    img = "https://generated.photos/vue-static/home/face-generator/face3.jpg"  # 기본 이미지

    # 조건별 스타일 분석
    if (
        a.get("Q1") == "강아지상 🐶"
        or a.get("Q2") == "연하 🧒"
        or a.get("Q3") == "다정 💗"
    ):
        img = "https://generated.photos/vue-static/home/face-generator/age-male-before.jpg"
        desc += """
        🐶 귀엽고 다정한 연하남  
        ☀️ 밝고 순수한 에너지!  
        💬 사소한 대화에도 귀 기울이는 센스쟁이
        """

    elif (
        a.get("Q1") == "고양이상 😼"
        or a.get("Q2") == "연상 👨‍💼"
        or a.get("Q3") == "츤데레 🙃"
    ):
        img = "https://generated.photos/vue-static/home/face-generator/face2.jpg"
        desc += """
        🖤 시크하고 강단 있는 고양이상  
        💼 눈빛으로 말하는 연상  
        🙃 다정함을 숨기고 행동으로 보여주는 츤데레
        """

    elif (
        a.get("Q4") == "무쌍 😌"
        or a.get("Q5") == "안경 유 🤓"
    ):
        img = "https://generated.photos/vue-static/home/face-generator/face4.jpg"
        desc += """
        📚 문학 감성의 조용한 매력  
        🤓 생각이 깊고, 듣는 걸 더 좋아하는 사람  
        ☕ 책과 음악을 사랑하는 혼자만의 시간 장인
        """

    elif (
        a.get("Q6") == "키 큰 👠"
        and a.get("Q3") == "다정 💗"
    ):
        img = "https://generated.photos/vue-static/home/face-generator/face5.jpg"
        desc += """
        🧸 듬직하고 따뜻한 키 큰 이상형  
        🌟 묵묵하지만 항상 곁에 있어주는 사람  
        🤲 포근한 말투에 안기고 싶은 느낌
        """

    else:
        desc += """
        🎮 장난도 잘 치고 분위기 메이커  
        😄 대화가 끊기지 않고 항상 웃게 되는 스타일  
        🎧 "같이 있으면 시간 순삭!" 같은 에너지 넘치는 사람
        """

    st.markdown("## 💘 당신에게 어울리는 이상형은 이런 느낌!")
    st.image(img, width=240, caption="✨ 이상형 이미지 (AI 생성)")
    st.markdown(desc.strip())
    st.balloons()

    if st.button("🔄 다시 하기"):
        reset()
