import random
import streamlit as st

st.set_page_config(
    page_title="사다리 타기 게임",
    page_icon="🎯",
    layout="centered"
)

st.title("🎯 사다리 타기 게임")
st.write("참가자와 결과를 입력하면 랜덤으로 연결해주는 웹 사다리 타기입니다.")

st.divider()

st.subheader("1️⃣ 참가자 입력")
players_text = st.text_area(
    "참가자 이름을 한 줄에 하나씩 입력하세요.",
    placeholder="민수\n철수\n영희\n지훈"
)

st.subheader("2️⃣ 결과 입력")
results_text = st.text_area(
    "결과를 한 줄에 하나씩 입력하세요.",
    placeholder="치킨\n피자\n꽝\n햄버거"
)

show_one_by_one = st.checkbox("결과를 하나씩 공개하기", value=False)

if st.button("🚀 사다리 타기 시작!", use_container_width=True):
    players = [p.strip() for p in players_text.splitlines() if p.strip()]
    results = [r.strip() for r in results_text.splitlines() if r.strip()]

    if len(players) == 0:
        st.error("참가자를 1명 이상 입력해주세요.")
    elif len(results) == 0:
        st.error("결과를 1개 이상 입력해주세요.")
    elif len(players) != len(results):
        st.error(f"참가자 수({len(players)}명)와 결과 수({len(results)}개)가 같아야 합니다.")
    else:
        random.shuffle(results)
        pairs = list(zip(players, results))

        st.success("사다리 타기 완료!")

        if show_one_by_one:
            st.subheader("🎁 결과 공개")
            for player, result in pairs:
                with st.expander(f"{player}님의 결과 보기"):
                    st.markdown(f"### {player} ➜ **{result}**")
        else:
            st.subheader("📜 전체 결과")
            for player, result in pairs:
                st.markdown(f"### {player} ➜ **{result}**")

st.divider()
st.caption("※ 재미용 랜덤 게임입니다.")
