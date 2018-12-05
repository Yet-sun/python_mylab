'''
需求：
编程实现一个21点扑克牌游戏程序，实现电脑AI和玩家的比拼。游戏规则如下：
a、现有一副扑克牌，第一轮双方各有两张随机分发的扑克牌，其中一张为底牌，只有自己知晓，对方只能看到另一张牌。
b、接下来每一轮，每位玩家可以选择继续随机摸一张牌或者叫停（即此轮该玩家不摸牌）
c、在某一轮中，若双方都叫停，则进行结果评定。谁的“点数和”越接近21点且不大于21点（等于21点为最大）为获胜方，凡是大于21点（称为“引爆”）或者“点数和”小于对方的“点数和”的一方为输。
d、大小王的点数为0。
e、J,Q,K的点数为10。
f、其余的点数都与自己所表示的数字一样。
要求：
a、要求采用模块化编程方法，对于相似功能的模块需要放入到一个包中。比如：发牌程序包、游戏判定包等等。每个包又包含几个模块。
b、电脑AI需要实现的主要智能包括：是否还要继续摸牌的判断。
c、游戏结束后，所有牌都可见，且显示胜利者

    @version : 1.0
'''

import random


# 1
def ask_user(prompt, response1, response2):
    """
    Ask user for a response in two responses.
    prompt (str) - The prompt to print to the user
    response1 (str) - One possible response that the user can give
    response2 (str) - Another possible response that the user can give
    """

    while True:
        # ask user for response
        user_response = input(prompt)

        # if response is response1 or response2 then return
        if user_response == response1 or user_response == response2:
            return user_response


# 2
def print_card(name, num):
    """
    print "______ draws a _____" with the first blank replaced by the user's
    name and the second blank replaced by the value given to the function.
    name (str) - the user name to print out
    num (int) - the number to print out
    """

    # if the value is a 1, 11, 12, 13, print Ace, Jack, Queen, King
    if num == 1:
        num = "Ace"
    elif num == 11:
        num = "Jack"
    elif num == 12:
        num = "Queen"
    elif num == 13:
        num = "King"
    else:
        num = str(num)

    # print the string
    print(name, "draws a", num)


# 3
def get_ace_value():
    """
    Ask the user if they want to use a 1 or 11 as their Ace value.
    """

    # get the value use "ask_user" function
    value = ask_user("Should the Ace be 1 or 11?", "1", "11")

    # retrun the value
    return int(value)


# 4
def deal_card(name):
    """
    Pick a random number between 1 and 13, and print out what the user drew.
    name (str) - the user name to print out
    """

    # get a random number in range 1 to 13
    num = random.randrange(1, 13 + 1)

    # use "print_card" function to print out what the user drew
    print_card(name, num)

    if num > 10:
        # if the card is a Jack, Queen, or King, the point-value is 10
        return 10
    elif num == 1:
        # If the card is an Ace, ask the user if the value should be 1 or 11
        return get_ace_value()
    else:
        return num


# 5
def adjust_for_bust(num):
    """
    If the given number is greater than 21, print "Bust!" and return -1.
    Otherwise return the number that was passed in.
    num (int) - the given number
    """

    # determine the value of num
    if num > 21:
        print("Bust!")
        return -1
    else:
        return num


# 6
def hit_or_stay(num):
    """
    Prompt the user hit or stay and return user's chose.
    num (int) - the value of a player's card hand
    """

    if num <= 21:
        chose = ask_user("Hit or stay?", "hit", "stay")
        # if num less than 21 and user chose hit return True
        if chose == "hit":
            return True

    # otherwise return False
    return False


# 7
def play_turn(name):
    """
    Play whole the trun for a user.
    name (str) - the player's name
    """

    # print out that it's the current players turn
    print("==========[ Current player:", name, "]==========")

    # set total score zero
    total_score = 0

    # deal the player a card for loop
    while True:

        # get total score
        total_score += deal_card(name)

        # if not busted print out the player's total score
        print("Total:", total_score)

        # if player chose stay return the result, otherwise continue the loop
        if not hit_or_stay(total_score):
            return adjust_for_bust(total_score)


# 8
def determine_winner(name1, name2, score1, score2):
    """
    Determine_the game's winner.
    name1 (str) - the first player's name
    name2 (str) - the second player's name
    score1 (str) - the first player's score
    score2 (str) - the second player's score
    """

    if score1 == score2:
        print(name1, "and", name2, "tie!")
    elif score1 > score2:
        print(name1, "wins!")
    elif score1 < score2:
        print(name2, "wins!")


# 9
def main():
    """
    The main program of BlackJack game
    """

    while True:

        # Ask each player for their name
        name1 = input("Player 1 name:")
        name2 = input("Player 2 name:")

        # Greet them
        print("Welcome to BlackJack", name1, "and", name2)
        print()

        # Let the first player play a turn
        score1 = play_turn(name1)
        print()

        # Let the second player play a turn
        score2 = play_turn(name2)
        print()

        # Determine who won
        determine_winner(name1, name2, score1, score2)

        # Play again if they say yes and end the loop if they say no
        if ask_user("Would you like to play again?", "yes", "no") == "no":
            break


if __name__ == "__main__":
    main()