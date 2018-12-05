from Lab_projects.lab8.l4.Licensing import licensing
from Lab_projects.lab8.l4.Print import *
from Lab_projects.lab8.l4.Judgment import *
import random


def main():
    """
    21点游戏主函数入口
    """

    while True:

        print("====[ “欢迎来到21点游戏人机对战” ]====")

        # 发底牌
        num11 = random.randrange(1, 13 + 1)
        num12 = random.randrange(1, 13 + 1)

        n1 = print_hidden_card.print_hidden_card_player(num11)
        n2 = print_hidden_card.print_hidden_card_AI(num12)
        print("===================================")
        num21 = random.randrange(1, 13 + 1)
        num22 = random.randrange(1, 13 + 1)

        while True:
            # while True:
            score2 = 0
            if score2 < 17:  # 如果电脑的牌面得分小于等于17则继续摸牌，否则直接判断此时的输赢
                p1 = []
                p2 = []
                p1.append(str(n1))  # 列表中加入底牌
                p1.append(",")
                p2.append(str(n2))
                p2.append(",")
                p = licensing.licensing_player(num21)  # 发牌给玩家
                a = licensing.licensing_AI(num22)  # 发牌给AI
                score1 = score.score_player(num11, num21)  # 计算玩家得分
                score2 = score.score_AI(num12, num22)  # 计算AI得分
                p1.append(str(p))  # 列表中加入发的牌
                p2.append(str(a))
                answer1 = input("是否继续摸牌？Y or N")
                if answer1 == "N":
                    print_all.print_player_all(p1)
                    print_all.print_AI_all(p2)
                    determine_winner.determine_winner(score1, score2)  # 判断赢家
                    break
                else:
                    continue

        print("===================================")
        print("再来一局？Y or N")
        answer2 = input()
        if answer2 == 'N':
            break


if __name__ == "__main__":
    main()
