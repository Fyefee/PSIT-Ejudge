"""<3 Jeffy"""
def main(text):
    """FourDirections"""
    for _ in text:
        print("  *  ", end=" ")
    print()
    for i in text:
        result = check2(i)
        print(result, end=" ")
    print()
    for i in text:
        result = check3(i)
        print(result, end=" ")
    print()
    for i in text:
        result = check4(i)
        print(result, end=" ")
    print()
    for _ in text:
        print("  *  ", end=" ")
    print()

def check2(text):
    """line 2"""
    if text == "U":
        result = " *** "
    elif text == "D":
        result = "  *  "
    elif text == "L":
        result = " *   "
    elif text == "R":
        result = "   * "
    return result

def check3(text):
    """line 3"""
    if text == "U":
        result = "* * *"
    elif text == "D":
        result = "* * *"
    elif text == "L":
        result = "*****"
    elif text == "R":
        result = "*****"
    return result

def check4(text):
    """line 4"""
    if text == "U":
        result = "  *  "
    elif text == "D":
        result = " *** "
    elif text == "L":
        result = " *   "
    elif text == "R":
        result = "   * "
    return result

main(input())
