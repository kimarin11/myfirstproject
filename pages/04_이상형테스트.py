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
        img = "https://img4.yna.co.kr/etc/inner/KR/2021/02/19/AKR20210219023200005_01_i_P4.jpg"
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
        img = "data:image/jpeg;base64,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"
        desc += """
        📚 문학 감성의 조용한 매력  
        🤓 생각이 깊고, 듣는 걸 더 좋아하는 사람  
        ☕ 책과 음악을 사랑하는 혼자만의 시간 장인
        """

    elif (
        a.get("Q6") == "키 큰 👠"
        and a.get("Q3") == "다정 💗"
    ):
        img = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/%E9%87%91%E5%96%84%E6%97%B4_%EA%B9%80%EC%84%A0%EC%9A%B0_sunwoo.jpg/1200px-%E9%87%91%E5%96%84%E6%97%B4_%EA%B9%80%EC%84%A0%EC%9A%B0_sunwoo.jpg"
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
