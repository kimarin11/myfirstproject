import streamlit as st

st.set_page_config(page_title="이상형 추천 테스트 💘", page_icon="💘", layout="centered")

st.title("💘 이상형 성향 테스트 💘")
st.markdown("당신의 취향을 하나하나 알아보며 이상형을 추천해드릴게요! 😍")

# 단계 관리
if 'step' not in st.session_state:
    st.session_state.step = 1
    st.session_state.answers = {}

def next_step():
    st.session_state.step += 1

def reset():
    st.session_state.step = 1
    st.session_state.answers = {}

questions = [
    ("고양이상 😼", "강아지상 🐶"),
    ("연상 👩", "동갑 👯", "연하 👶"),
    ("다정 💗", "츤데레 🙃"),
    ("무쌍 😌", "속쌍 😉", "유쌍 🥰"),
    ("안경 유 🤓", "안경 무 😎"),
    ("키 큰 👠", "키 작은 👟")
]

# 질문 진행
step = st.session_state.step
total = len(questions)

if step <= total:
    q = questions[step - 1]
    st.markdown(f"### Q{step}. 당신의 취향은?")
    choice = st.radio("선택하세요 👇", q, key=f"q{step}")
    if st.button("다음 👉"):
        st.session_state.answers[f"Q{step}"] = choice
        next_step()
else:
    st.success("🎉 모든 질문이 완료되었습니다!")
    st.markdown("당신의 취향에 맞춘 이상형을 추천해드릴게요! 💖")

    a = st.session_state.answers  # 선택 저장된 dict

    # 결과 간단 매칭 (예시)
    result = "💘 당신의 이상형은...\n\n"
    if a.get("Q1") == "강아지상 🐶":
        result += "🐶 따뜻한 눈빛과 귀여운 행동의 강아지상!\n"
    else:
        result += "😼 시크하고 매혹적인 고양이상!\n"

    if a.get("Q2") == "연상 👩":
        result += "👩 연상의 매력, 믿음직하고 어른스러운 스타일!\n"
    elif a.get("Q2") == "동갑 👯":
        result += "👯 친구처럼 편한 동갑 스타일!\n"
    else:
        result += "👶 귀엽고 상큼한 연하 스타일!\n"

    if a.get("Q3") == "다정 💗":
        result += "💗 언제나 살가운 다정함에 심쿵~\n"
    else:
        result += "🙃 표현은 서툴지만 진심 있는 츤데레 매력!\n"

    if a.get("Q4") == "무쌍 😌":
        result += "😌 깊고 오묘한 눈매가 매력적인 무쌍!\n"
    elif a.get("Q4") == "속쌍 😉":
        result += "😉 감춰진 매력 속쌍 아이!\n"
    else:
        result += "🥰 눈웃음이 사랑스러운 유쌍!\n"

    if a.get("Q5") == "안경 유 🤓":
        result += "🤓 스마트함의 대명사 안경 스타일!\n"
    else:
        result += "😎 세련되고 시크한 안경 없는 스타일!\n"

    if a.get("Q6") == "키 큰 👠":
        result += "👠 모델핏의 키 큰 이상형!\n"
    else:
        result += "👟 작고 귀여운 키 작은 스타일!\n"

    st.markdown(f"### 💖 결과\n{result}")
    st.toast("이상형 분석 완료! 💘", icon="🔍")
    st.balloons()
    st.snow()

    if st.button("🔄 다시 해보기"):
        reset()
