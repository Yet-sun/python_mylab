'''
打印底牌
'''
from Lab_projects.lab8.l4.Print import print_card


def print_hidden_card_player(num1):
    name1 = "你的底牌"
    num1 = print_card.print_card(name1, num1)

    return num1


def print_hidden_card_AI(num2):
    name2 = "电脑的底牌"
    print_card.print_card(name2, num2)

    return num2
