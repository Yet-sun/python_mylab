'''
计算得分
'''
from Lab_projects.lab8.l4.Judgment import judgment

def score_player(num11, num21):
    num11=int(judgment.judge_player(num11))
    score = num11
    score += num21
    if score > 21:
        print("你的牌被引爆了！")
        return None
    else:
        return score


def score_AI(num12, num21):
    num12=int(judgment.judge_AI(num12))
    score = num12
    score += num21

    return score
