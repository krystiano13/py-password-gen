charAmount = 0
containUpperCase = False
containNumbers = False
containSpecial = False

def askUpperCase():
    upper = input("Should your password contain upperCase characters ? [true/false]")

    if upper == "true":
        return True
    elif upper == "false":
        return False
    else:
        print("Wrong answer provided")
        return askUpperCase()

def getCharAmount():
    print("How many characters your password should have ? \n")
    try:
        chars = input("Insert integer number larger than 0:")
        num = int(chars)
    except ValueError:
        print("Value is not an integer number")
        return getCharAmount()
    return chars

charAmount = getCharAmount()
containUpperCase = askUpperCase()