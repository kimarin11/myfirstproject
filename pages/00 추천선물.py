import streamlit as st

st.set_page_config(page_title="이상형 테스트 💘", page_icon="💘", layout="centered")

st.title("💘 이상형 성향 테스트")
st.markdown("당신의 취향을 하나씩 골라보세요! 💫\n완성되면 당신에게 딱 어울리는 이상형을 보여드릴게요!")

# 상태 초기화
if 'step' not in st.session_state:
    st.session_state.step = 1
    st.session_state.answers = {}

questions = [
    ("고양이상 😼", "강아지상 🐶"),
    ("연상 👨‍💼", "동갑 👨", "연하 🧒"),
    ("다정 💗", "츤데레 🙃"),
    ("무쌍 😌", "속쌍 😉", "유쌍 🥰"),
    ("안경 유 🤓", "안경 무 😎"),
    ("키 큰 👠", "키 작은 👟")
]

def reset():
    st.session_state.step = 1
    st.session_state.answers = {}

# 현재 질문
step = st.session_state.step
total = len(questions)

if step <= total:
    q = questions[step - 1]
    st.markdown(f"### Q{step}. 당신의 취향은?")
    selected = st.radio("선택하세요 👇", q, key=f"radio_{step}")
    if st.button("다음 👉"):
        st.session_state.answers[f"Q{step}"] = selected
        st.session_state.step += 1
else:
    st.success("🎉 테스트 완료!")
    st.toast("당신에게 어울리는 이상형을 찾는 중... 💘", icon="🔍")
    st.snow()

    a = st.session_state.answers

    # 캐릭터 추천 매칭 (이름 없이 이미지와 설명만!)
    if (
        a.get("Q1") == "강아지상 🐶"
        and a.get("Q2") == "연하 🧒"
        and a.get("Q3") == "다정 💗"
        and a.get("Q5") == "안경 유 🤓"
    ):
        img = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Sample_User_Icon.png/240px-Sample_User_Icon.png"
        desc = """
        🐶 부드러운 말투와 다정한 눈빛의 연하남  
        🤓 조용히 옆에 앉아 책을 읽거나, 몰래 간식 챙겨주는 타입  
        💬 “오늘 하루 어땠어요?” 같은 소소한 배려에 녹아내리는 스타일
        """
    elif (
        a.get("Q1") == "고양이상 😼"
        and a.get("Q2") == "연상 👨‍💼"
        and a.get("Q3") == "츤데레 🙃"
    ):
        img = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Profile_avatar_placeholder_large.png/240px-Profile_avatar_placeholder_large.png"
        desc = """
        🖤 차갑지만 섬세한 감정을 가진 고양이상  
        🙃 말수는 적지만 진심을 눈빛에 담는 츤데레 연상  
        ☕ 카페 한쪽에서 책 읽는 모습, 왠지 그냥 설레요
        """
    else:
        img = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/240px-No_image_available.svg.png"
        desc = """
        🎧 유쾌하고 말 잘 통하는 동갑 친구 같은 사람  
        😆 가벼운 농담도 깊은 고민도 나눌 수 있는 편안함  
        🎮 오락실에서 춤추며 웃는 얼굴이 잊히지 않아요
        """

    # 결과 표시
    st.markdown("## ✨ 당신의 이상형은 이런 느낌!")
    st.image(img, use_column_width=False, width=200)
    st.markdown(desc)
    st.balloons()

    if st.button("🔄 다시 하기"):
        reset()
