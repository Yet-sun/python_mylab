'''
需求：编写程序解决豆堆问题。
    豆堆里有16颗豆子，有两个玩家（假设一个玩家是电脑）。
    每个玩家都可以从堆中的16颗豆子中取出1颗，2颗或者3颗豆子。
    每个玩家在每回合中必须从堆中取出一定数目的豆子。
    玩家轮流取出豆子，取到最后一颗豆子的玩家是输家。
思路：
    写一个人取豆子的函数
    帮电脑设计一个算法，实现取豆子的函数
    在主程序中进行输流调用，谁最后拿到1粒豆子谁就输。
'''
import random


def takeBean(total: int) -> int:
    while True:
        num = int(input("请取出1-3粒豆子："))
        if num < 1 or num > 3:
            print("只能取出1-3粒豆子")
            continue
        return (total - num)


def opponentTakeBean(n: int) -> int:
    if n == 2:
        return 1
    if n == 3:
        return 2
    if n == 4:
        return 3
    else:
        i = random.randint(1, 3)
        return i


def main():
    total = 16
    while True:
        leftBeanPeople = takeBean(total)
        leftBeanOpponent = opponentTakeBean(leftBeanPeople)
        total = leftBeanPeople - leftBeanOpponent
        if leftBeanPeople == 1:
            print("获胜!")
            break
        print("对手取出" + str(leftBeanOpponent) + "粒豆子,还剩" + str(total) + "粒豆子")
        if total == 1:
            print("失败！")
            break


main()
