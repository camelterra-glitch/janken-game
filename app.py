import random
import streamlit as st

st.title("✊✌️🖐 じゃんけんゲーム")

wins = {"グー": "チョキ", "チョキ": "パー", "パー": "グー"}

# スコアの初期化
if "win" not in st.session_state:
    st.session_state.win = 0
if "lose" not in st.session_state:
    st.session_state.lose = 0
if "draw" not in st.session_state:
    st.session_state.draw = 0
if "streak" not in st.session_state:
    st.session_state.streak = 0
if "best_streak" not in st.session_state:
    st.session_state.best_streak = 0

st.subheader("手を選んでください")
col1, col2, col3 = st.columns(3)

player = None
with col1:
    if st.button("✊ グー"):
        player = "グー"
with col2:
    if st.button("✌️ チョキ"):
        player = "チョキ"
with col3:
    if st.button("🖐 パー"):
        player = "パー"

if player:
    computer = random.choice(["グー", "チョキ", "パー"])
    st.write(f"あなた：**{player}**　コンピュータ：**{computer}**")

    if player == computer:
        st.info("引き分け！")
        st.session_state.draw += 1
        st.session_state.streak = 0
    elif wins[player] == computer:
        st.success("あなたの勝ち！🎉")
        st.session_state.win += 1
        st.session_state.streak += 1
        if st.session_state.streak > st.session_state.best_streak:
            st.session_state.best_streak = st.session_state.streak
    else:
        st.error("コンピュータの勝ち！😢")
        st.session_state.lose += 1
        st.session_state.streak = 0

st.divider()
st.subheader("スコア")
st.write(f"勝ち：{st.session_state.win}　負け：{st.session_state.lose}　引き分け：{st.session_state.draw}")

st.subheader("連勝記録")
st.write(f"現在の連勝：{st.session_state.streak}　最高連勝：{st.session_state.best_streak}")

if st.button("リセット"):
    st.session_state.win = 0
    st.session_state.lose = 0
    st.session_state.draw = 0
    st.session_state.streak = 0
    st.session_state.best_streak = 0