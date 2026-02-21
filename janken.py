import random

def get_computer_choice():
    return random.choice(["グー", "チョキ", "パー"])

def judge(player, computer):
    if player == computer:
        return "引き分け"
    wins = {"グー": "チョキ", "チョキ": "パー", "パー": "グー"}
    return "あなたの勝ち！" if wins[player] == computer else "コンピュータの勝ち！"

def main():
    print("=== じゃんけんゲーム ===")
    choices = {"1": "グー", "2": "チョキ", "3": "パー"}
    
    while True:
        print("\n1: グー  2: チョキ  3: パー  q: 終了")
        user_input = input("選んでください: ")
        
        if user_input == "q":
            print("ゲームを終了します。")
            break
        if user_input not in choices:
            print("1, 2, 3 のいずれかを入力してください。")
            continue
        
        player = choices[user_input]
        computer = get_computer_choice()
        
        print(f"あなた: {player}  コンピュータ: {computer}")
        print(judge(player, computer))

if __name__ == "__main__":
    main()