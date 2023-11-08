def getInfo(dataType):
    inputText = "Should your password contain {0} characters ? [true/false]".format(dataType)
    value = input(inputText)
    if value == "true":
        return True
    elif value == "false":
        return False
    else:
        print("Wrong answer provided")
        return getInfo(dataType)
