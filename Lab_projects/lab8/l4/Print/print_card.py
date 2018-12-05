def print_card(name,num):
    # 值为 0, 1, 11, 12, 13时, 打印出Jokers, Ace, Jack, Queen, King
    if num == 0:
        num = "Jokers"  # 大小王
    elif num == 1:
        num = "Ace"
    elif num == 11:
        num = "Jack"
    elif num == 12:
        num = "Queen"
    elif num == 13:
        num = "King"
    else:
        num = str(num)

    print(name,"的牌点数为：", num)

    return num
