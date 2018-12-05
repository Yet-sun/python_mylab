def determine_winner(score1, score2):
    if score1 == score2:
        print("平局")
    elif score1 > score2:
        print("你获得了胜利！！！")
    else:
        print("你输了！")
