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
        img = "https://www.google.com/search?q=%EC%B0%A8%EC%9D%80%EC%9A%B0&sca_esv=5ccc3c2961696a5e&sxsrf=AE3TifP6sLduv99Lj0O2C__IPWDJC164Fg%3A1748670817134&source=hp&ei=YZk6aOCIBumP2roPr4nj0Ag&iflsig=AOw8s4IAAAAAaDqncaN7TkX8ihJKskNrVBV3MvokJnqz&udm=2&oq=&gs_lp=Egdnd3Mtd2l6IgAqAggAMg0QIxjwBRgnGMkCGOoCMg0QIxjwBRgnGMkCGOoCMgcQIxgnGOoCMgoQIxjwBRgnGOoCMgcQIxgnGOoCSPaWGlAAWABwAngAkAEAmAEAoAEAqgEAuAEByAEAmAICoAIKqAIFmAMF8QUkucttWqQ3D_EFolSletpgccuSBwEyoAcAsgcAuAcAwgcDMi0yyAcH&sclient=gws-wiz#vhid=EJlUPQMXwHaGxM&vssid=mosaic"
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
        img = "https://www.google.com/search?sca_esv=5ccc3c2961696a5e&sxsrf=AE3TifPSM6tMyDln4enab2Nsqif9zMxS3A:1748671381357&q=%EC%9E%A5%ED%95%98%EC%98%A4&udm=2&fbs=AIIjpHyDg0Pef0CibV20xjIa-FRejxCuOmkq074km2sZXr7uq8hqY3b-NkqmHBgKS9xzRFsJd68YxnQqXZ0YI1vLWbx74P-HB5jYNR9ehU8zZhY1pWhcvPw7aR-heDa0orPab1TP0i2_PzHNln7I_ZkijyAwa9m7mTmhgsA81udzFrmej0rKfD-7hH3l1dcilj8zXDAy8Mbhh8FDG-UfB7lwTNeBScjTf3rfgQvkjCJ5K_fbeHn8YSQ&sa=X&ved=2ahUKEwjk347EhM2NAxXqavUHHZG6DrwQtKgLegQIHBAB&biw=1707&bih=944&dpr=1.5#vhid=zXAlw_0-_yHrrM&vssid=mosaic"
        desc = """
        🖤 차가운 듯 다정한 연상 고양이상  
        💼 말보다 행동으로 표현하는 츤데레  
        ☕ 혼자 있어도 멋진, 묘하게 끌리는 사람
        """
    elif a.get("Q5") == "안경 유 🤓" and a.get("Q4") == "무쌍 😌":
        img = "https://www.google.com/search?q=%EA%B9%80%EC%9D%B4%ED%95%9C+%EC%95%88%EA%B2%BD&sca_esv=5ccc3c2961696a5e&udm=2&biw=1707&bih=944&sxsrf=AE3TifPmST1_AdsS_aC-4HbpXV4ypGDIVQ%3A1748671426657&ei=wps6aKnwJ-TH1e8P8uS82AU&ved=0ahUKEwip2dvZhM2NAxXkY_UHHXIyD1sQ4dUDCBE&uact=5&oq=%EA%B9%80%EC%9D%B4%ED%95%9C+%EC%95%88%EA%B2%BD&gs_lp=EgNpbWciEOq5gOydtO2VnCDslYjqsr1IqxRQ3gZYtRNwAngAkAECmAF_oAHWDaoBBDAuMTW4AQPIAQD4AQGYAgagAuQDqAIFwgIKECMYJxjJAhjqAsICCxAAGIAEGLEDGIMBwgIEEAAYA8ICBRAAGIAEwgIHECMYJxjJAsICCBAAGIAEGLEDmAMDkgcDMi40oAeoMbIHAzAuNLgH3QPCBwcwLjIuMy4xyAcY&sclient=img#vhid=xhqy3y4BPN5nGM&vssid=mosaic"
        desc = """
        📚 문학 감성의 지적인 이상형  
        🎧 조용한 곳에서 음악 들으며 산책하는 걸 좋아해요  
        😌 시선은 차분하지만 마음은 따뜻한 사람
        """
    else:
        img = "https://www.google.com/search?q=%EA%B9%80%EC%84%A0%EC%9A%B0&sca_esv=5ccc3c2961696a5e&udm=2&biw=1707&bih=944&sxsrf=AE3TifNgkfX-tsamRgylXfSZGQbtt3ofug%3A1748671443139&ei=05s6aJ6eCNbDvr0PmePu4QQ&ved=0ahUKEwje08nhhM2NAxXWoa8BHZmxO0wQ4dUDCBE&uact=5&oq=%EA%B9%80%EC%84%A0%EC%9A%B0&gs_lp=EgNpbWciCeq5gOyEoOyasDIIEAAYgAQYsQMyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDILEAAYgAQYsQMYgwEyBRAAGIAEMgUQABiABDIFEAAYgARIsRNQAFixEnAEeACQAQCYAfgDoAH0DKoBCzAuNy4wLjEuMC4xuAEDyAEA-AEBmAILoAK-C6gCBsICChAjGCcYyQIY6gLCAgQQABgDwgIHECMYJxjJApgDA5IHCTQuNS4wLjEuMaAHuyyyBwkwLjUuMC4xLjG4B7ALwgcFMC4yLjnIBy8&sclient=img#vhid=XyNPxKfV25ttqM&vssid=mosaic"
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
