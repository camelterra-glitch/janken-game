import random
import streamlit as st

st.title("✊✌️🖐 じゃんけんゲーム")

wins = {"グー": "チョキ", "チョキ": "パー", "パー": "グー"}
beats = {"グー": "パー", "チョキ": "グー", "パー": "チョキ"}

def get_computer_choice(level, history):
    if level == "弱い":
        # 完全ランダム
        return random.choice(["グー", "チョキ", "パー"])
    
    elif level == "普通":
        # 70%ランダム、30%パターン読み
        if len(history) < 3 or random.random() < 0.7:
            return random.choice(["グー", "チョキ", "パー"])
        most_common = max(set(history[-5:]), key=history[-5:].count)
        return beats[most_common]
    
    else:  # 強い
        # 履歴が少ない間はランダム
        if len(history) < 3:
            return random.choice(["グー", "チョキ", "パー"])
        # 直近5回で一番多い手に勝つ手を出す
        most_common = max(set(history[-5:]), key=history[-5:].count)
        return beats[most_common]

# セッションの初期化
for key, val in [("win", 0), ("lose", 0), ("draw", 0),
                 ("streak", 0), ("best_streak", 0), ("history", [])]:
    if key not in st.session_state:
        st.session_state[key] = val

# 難易度選択
level = st.radio("コンピュータの強さを選んでください", ["弱い", "普通", "強い"], horizontal=True)

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
    st.session_state.history.append(player)
    computer = get_computer_choice(level, st.session_state.history)
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
    st.session_state.history = []