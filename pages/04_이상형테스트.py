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
    # 예시 조합별 결과 (단 3가지 결과만 보여줬던 걸 개선)
    if (
        a.get("Q1") == "강아지상 🐶"
        and a.get("Q2") == "연하 🧒"
        and a.get("Q3") == "다정 💗"
    ):
        # 부드럽고 따뜻한 연하 강아지상
        img = "https://storage.blip.kr/topic/a51b27715cd8f7206dd23f8e9fc923b1.jpg"
        desc = "🐶 귀엽고 다정한 연하남..."
    elif (
        a.get("Q1") == "고양이상 😼"
        and a.get("Q2") == "연상 👨‍💼"
        and a.get("Q3") == "츤데레 🙃"
    ):
        # 차가운 연상 고양이상
        img = "https://storage.blip.kr/topic/a51b27715cd8f7206dd23f8e9fc923b1.jpg"
        desc = "🖤 말보다 눈빛으로 말하는 츤데레형..."
    elif a.get("Q5") == "안경 유 🤓" and a.get("Q4") == "무쌍 😌":
        # 지적이고 부드러운 분위기의 남자
        img = "https://storage.blip.kr/topic/a51b27715cd8f7206dd23f8e9fc923b1.jpg"
        desc = "📚 책 냄새 좋아하는 문학 감성남..."
    elif a.get("Q6") == "키 큰 👠" and a.get("Q3") == "다정 💗":
        # 따뜻하고 믿음직한 키큰 남자
        img = "https://storage.blip.kr/topic/a51b27715cd8f7206dd23f8e9fc923b1.jpg"
        desc = "🧸 포옹이 포근한 듬직한 사람..."
    else:
        # 기본형
        img = "https://storage.blip.kr/topic/a51b27715cd8f7206dd23f8e9fc923b1.jpg"
        desc = "🎮 장난도 잘 치고 분위기 메이커..."


    # 결과 표시
    st.markdown("## 💘 당신에게 어울리는 이상형은 이런 느낌!")
    st.image(img, use_column_width=False, width=240, caption="✨ 이상형 이미지 (AI 생성)")
    st.markdown(desc)
    st.balloons()

    if st.button("🔄 다시 하기"):
        reset()
