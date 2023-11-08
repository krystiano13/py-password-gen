def getInfo(dataType):
    inputText = ""
    match dataType:
        case "numbers":
            inputText = "Should your password contain number characters ? [true/false]"
        case "uppercase":
            inputText = "Should your password contain upperCase characters ? [true/false]"
        case "special":
            inputText = "Should your password contain special characters ? [true/false]"

    value = input(inputText)
    if value == "true":
        return True
    elif value == "false":
        return False
    else:
        print("Wrong answer provided")
        return getInfo(dataType)
