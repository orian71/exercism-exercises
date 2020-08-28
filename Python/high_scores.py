def latest(list):
    if len(list) > 0:
        return list[len(list)-1]
    else:
        return "List is empty."

def personal_best(list):
    if len(list) > 1:
        return max(list)
    else:
        return list

def personal_top_three(list):
    if len(list) == 0:
        return "Input list is empty."
    else:
        result = sorted(list)[-3:]
        return sorted(result,key=None,reverse=True)