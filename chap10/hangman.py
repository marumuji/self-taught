def hangman(word):
    wrong = 0
    stages = ["",
              "___________      ",
              "|                ",
              "|          |     ",
              "|          O     ",
              "|         /|\    ",
              "|         / \    ",
              "|                "
             ]       
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "１文字を予想してね"
        char = input(msg)
        if char in rletters:
            index = rletters.index(char)
            rletters[index] = "$"
            board[index] = char
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1 # 不明
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))         
        print("あなたの負け！正解は{}.", word)

hangman("cat")
