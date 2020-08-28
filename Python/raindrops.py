def convert(number):
    result = ""
    if number % 3 == 0:
        result += "Pling"
        return result
    if number % 5 == 0:
        result += "Plang"
        return result
    if number % 7 == 0:
        result += "Plong"
        return result
    else:
        return str(number)