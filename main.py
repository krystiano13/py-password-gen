from info import getInfo
from rand_char import randChar

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
    return int(chars)

charAmount = getCharAmount()
containUpperCase = getInfo("upper case")
containNumbers = getInfo("number")
containSpecial = getInfo("special")
result = ""

for i in range(charAmount):
    result += randChar(containUpperCase, containNumbers, containSpecial)
print(result)
