'''
Licensing：发牌
'''

from Lab_projects.lab8.l4.Print import *

def licensing_player(num1):
    name="你"
    card = print_card.print_card(name,num1)

    return card


def licensing_AI(num2):
    name = "AI"
    card = print_card.print_card(name,num2)

    return card