import streamlit as st

st.set_page_config(page_title="이상형 추천 테스트 💘", page_icon="💌", layout="centered")

st.title("💘 당신의 취향으로 추천하는 이상형 💘")
st.subheader("한 가지 질문을 선택하면, 거기에 어울리는 인물을 추천해드릴게요!")

question = st.selectbox(
    "🎯 하나를 선택해보세요!",
    [
        "고양이상 😼 vs 강아지상 🐶",
        "연상 👩 vs 동갑 👯 vs 연하 👶",
        "다정 💗 vs 츤데레 🙃",
        "무쌍 😌 vs 속쌍 😉 vs 유쌍 🥰",
        "안경 유 🤓 vs 안경 무 😎",
        "키 큰 👠 vs 키 작은 👟"
    ]
)

# 추천 로직
recommend = {
    "고양이상 😼 vs 강아지상 🐶": {
        "추천": "🐶 강아지상: 민호 — 따뜻한 눈빛, 귀여운 말투, 안아주고 싶은 스타일! 💞",
        "효과": "balloons"
    },
    "연상 👩 vs 동갑 👯 vs 연하 👶": {
        "추천": "👩 연상: 지혜롭고 어른스러운, 믿고 기대고 싶은 이상형! 🧡",
        "효과": "snow"
    },
    "다정 💗 vs 츤데레 🙃": {
        "추천": "💗 다정: 하루 종일 ‘괜찮아?’라고 묻는 스윗한 말투에 심쿵! 🍬",
        "효과": "balloons"
    },
    "무쌍 😌 vs 속쌍 😉 vs 유쌍 🥰": {
        "추천": "🥰 유쌍: 눈웃음이 반칙! 마주치면 두근두근 ❤️‍🔥",
        "효과": "toast"
    },
    "안경 유 🤓 vs 안경 무 😎": {
        "추천": "🤓 안경 유: 스마트한 매력 폭발! 안경 너머 눈빛에 녹는다... 🫠",
        "효과": "toast"
    },
    "키 큰 👠 vs 키 작은 👟": {
        "추천": "👟 키 작은: 작고 귀엽고 보호본능 자극! 같이 있으면 폭신한 느낌 🍮",
        "효과": "balloons"
    }
}

result = recommend.get(question)

st.markdown(f"## 💡 추천 이상형")
st.markdown(f"**{result['추천']}**")

# 💥 효과 최대화!
if result["효과"] == "balloons":
    st.balloons()
    st.toast("이상형이랑 같이 놀고 싶다... 🥺", icon="💓")
elif result["효과"] == "snow":
    st.snow()
    st.toast("마음이 녹는 스윗함... 💘", icon="☃️")
elif result["효과"] == "toast":
    st.toast("심장이 콩닥콩닥해요! 💗", icon="💓")
    st.toast("이런 사람, 어디 없을까요...? 😭", icon="🔍")
