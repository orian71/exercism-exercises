def is_armstrong_number(number):
    counter = 0
    numlist = [int(x) for x in str(number)]
    for i in numlist:
        counter += pow(i,len(numlist))
    if counter == number:
        return True
    else:
        return False