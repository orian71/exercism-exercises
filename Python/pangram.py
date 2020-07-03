def is_pangram(sentence):
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    letters = list(sentence)
    if sentence == "":
        return False
    else:
        for i in letters:
            if i in lowercase:
                del uppercase[lowercase.index(i)]
                lowercase.remove(i)
            elif i in uppercase:
                del lowercase[uppercase.index(i)]
                uppercase.remove(i)
            else:
                pass
        if len(lowercase) == 0 and len(uppercase) == 0:
            return True
        else:
            return False