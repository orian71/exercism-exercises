def latest(scores=[]):
    if len(scores) > 1:
        return scores[-1]
    else:
        return

def personal_best(scores=[]):
    if len(scores) > 1:
        best = scores[0]
        for i in scores:
            if i > best:
                best = i
            else:
                pass
        return best
    else:
        return

def personal_top_three(scores=[]):
    f = 0
    s = 0
    t = 0
    print(scores)
    if len(scores) == 0:
        return []
    elif len(scores) == 1:
        return scores
    elif len(scores) == 2:
        if scores[0] == scores[1]:
            return scores
        elif scores[0] > scores[1]:
            return scores
        else:
            return [scores[1], scores[0]]
    else:
        for a in scores:
            if a > f:
                f = a
            else:
                pass
        scores.remove(f)
        print(scores)
        for b in scores:
            if b >= s and b <= f and b >= t:
                s = b
            else:
                pass
        scores.remove(s)
        print(scores)
        for c in scores:
            if c >= t and c <= f and c <= s:
                t = c
            else:
                pass
        scores.remove(t)
        print(scores)
    return [f,s,t]
