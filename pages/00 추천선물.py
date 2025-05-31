import streamlit as st

st.set_page_config(page_title="이상형 성향 테스트 💘", page_icon="💘", layout="centered")
st.title("💘 이상형 성향 테스트")
st.markdown("당신의 취향을 하나하나 알아보며, 그에 어울리는 캐릭터를 추천해드릴게요! 😍")

# 상태 초기화
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
    st.success("🎉 모든 질문 완료!")
    st.markdown("## 🧠 분석 중...")
    st.toast("취향 데이터를 분석하는 중이에요! 💘", icon="🧬")
    st.snow()

    a = st.session_state.answers

    # 캐릭터 매칭 간단 로직 (예시 3명)
    if (
        a.get("Q1") == "강아지상 🐶"
        and a.get("Q2") == "연하 👶"
        and a.get("Q3") == "다정 💗"
        and a.get("Q5") == "안경 유 🤓"
    ):
        # 캐릭터 1: 민규
        name = "🐾 민규 (Mingyu)"
        desc = "항상 먼저 연락하고, 툭하면 웃어주는 강아지 같은 연하남 💌\n책 읽는 걸 좋아하고, 가끔 안경을 쓱 고치는 습관이 있어요. 무심한 듯 다정한 눈빛에 설렘 폭발! 🐶📖"
        img = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Sample_User_Icon.png/240px-Sample_User_Icon.png"
        st.image(img, caption="📸 캐릭터 이미지 (예시)", width=150)
        st.markdown(f"### ❤️ 당신의 이상형은:\n{name}\n{desc}")
        st.balloons()

    elif (
        a.get("Q1") == "고양이상 😼"
        and a.get("Q3") == "츤데레 🙃"
        and a.get("Q2") == "연상 👩"
    ):
        # 캐릭터 2: 소희
        name = "😼 소희 (Sohee)"
        desc = "처음엔 차갑지만 알면 알수록 따뜻한 츤데레 연상녀 💼\n눈꼬리가 살짝 올라간 고양이상. 커피 한 잔 들고 책 읽는 모습이 멋있어요. 말수는 적지만, 눈빛에 다 담겨 있어요. ☕📚"
        img = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Profile_avatar_placeholder_large.png/240px-Profile_avatar_placeholder_large.png"
        st.image(img, caption="📸 캐릭터 이미지 (예시)", width=150)
        st.markdown(f"### ❤️ 당신의 이상형은:\n{name}\n{desc}")
        st.toast("츤데레 + 고양이상 = 최강 조합! 😼💘")

    else:
        # 캐릭터 3: 지원
        name = "🌟 지원 (Jiwon)"
        desc = "애매한 듯 확실한 매력의 동갑 친구 스타일! 🎧\n대화가 잘 통하고, 같이 노는 게 즐거운 편안한 사람. 유쌍 눈웃음이 매력 포인트! 종종 장난도 치는 다정함에 무장해제 돼요. 😆"
        img = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/240px-No_image_available.svg.png"
        st.image(img, caption="📸 캐릭터 이미지 (예시)", width=150)
        st.markdown(f"### ❤️ 당신의 이상형은:\n{name}\n{desc}")
        st.toast("편안하고 귀여운 스타일이 딱이네요! 😍")

    if st.button("🔄 다시 해보기"):
        reset()
