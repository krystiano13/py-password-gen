def askSpecial():
    spec = input("Should your password contain special characters ? [true/false]")
    if spec == "true":
        return True
    elif spec == "false":
        return False
    else:
        print("Wrong answer provided")
        return askSpecial()

def askNumbers():
    num = input("Should your password contain number characters ? [true/false]")
    if num == "true":
        return True
    elif num == "false":
        return False
    else:
        print("Wrong answer provided")
        return askNumbers()

def askUpperCase():
    upper = input("Should your password contain upperCase characters ? [true/false]")

    if upper == "true":
        return True
    elif upper == "false":
        return False
    else:
        print("Wrong answer provided")
        return askUpperCase()
