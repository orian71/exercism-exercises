""" fourth iteration 10/18/2020 """

def latest(scores):
    return scores[-1:][0]

def personal_best(scores):
    return max(scores)

def personal_top_three(scores):
    return sorted(scores,key=None,reverse=True)[0:3]
