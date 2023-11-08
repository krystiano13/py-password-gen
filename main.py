from info import getInfo

charAmount = 0
containUpperCase = False
containNumbers = False
containSpecial = False

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
containUpperCase = getInfo("uppercase")
containNumbers = getInfo("numbers")
containSpecial = getInfo("special")