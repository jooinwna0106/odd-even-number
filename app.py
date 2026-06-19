import streamlit as st
import random

st.set_page_config(
    page_title="🎲 홀짝 게임",
    page_icon="🎲",
    layout="centered"
)

# CSS
st.markdown("""
<style>
.main {
    text-align: center;
}

.stButton > button {
    width: 100%;
    height: 60px;
    font-size: 24px;
    font-weight: bold;
    border-radius: 15px;
}

.result-box {
    padding: 20px;
    border-radius: 15px;
    background-color: #161B22;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# 게임머니 초기화
if "money" not in st.session_state:
    st.session_state.money = 1000

st.title("🎲 홀짝 게임")
st.write("1000 포인트로 시작!")

st.metric("💰 현재 포인트", st.session_state.money)

choice = st.radio(
    "홀 또는 짝 선택",
    ["홀", "짝"],
    horizontal=True
)

bet = st.number_input(
    "베팅 포인트",
    min_value=10,
    max_value=st.session_state.money if st.session_state.money > 0 else 10,
    value=100,
    step=10
)

if st.button("🎰 베팅하기"):

    number = random.randint(1, 100)

    result = "홀" if number % 2 else "짝"

    st.markdown(
        f"""
        <div class="result-box">
        <h2>🎲 나온 숫자: {number}</h2>
        <h2>결과: {result}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    if choice == result:
        st.session_state.money += bet
        st.success(f"🎉 승리! +{bet} 포인트")
    else:
        st.session_state.money -= bet
        st.error(f"😭 패배! -{bet} 포인트")

    if st.session_state.money <= 0:
        st.warning("💀 GAME OVER")
        st.session_state.money = 1000
        st.info("포인트가 1000으로 초기화되었습니다.")

st.divider()

if st.button("🔄 게임 리셋"):
    st.session_state.money = 1000
    st.rerun()
