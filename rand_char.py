from random import randint
def randChar(upper, num, special):
    randNum = randint(0, 3)

    match randNum:
        case 0:
            char = randint(97, 122)
            return chr(char)
        case 1:
            if not upper:
                return randChar(upper, num, special)
            else:
                char = randint(65, 90)
                return chr(char)
        case 2:
            if not num:
                return randChar(upper, num, special)
            else:
                char = randint(0, 9)
                return char
        case 3:
            if not special:
                return randChar(upper, num, special)
            else:
                char = randint(33, 47)
                return chr(char)