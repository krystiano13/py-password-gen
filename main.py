charAmount = 0

def getCharAmount():
    print("How many characters your password should have ? \n")
    chars = input("Insert number larger than 0:")
    return chars

charAmount = getCharAmount()
print(charAmount)