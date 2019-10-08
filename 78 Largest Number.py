"""<3 Jeffy"""
def main(num1, num2, num3):
    """Largest Number"""
    case1 = int(num1 + num2 + num3)
    case2 = int(num1 + num3 + num2)
    case3 = int(num2 + num1 + num3)
    case4 = int(num2 + num3 + num1)
    case5 = int(num3 + num1 + num2)
    case6 = int(num3 + num2 + num1)
    numhigh = high(case1, case2)
    numhigh2 = high(case3, case4)
    numhigh3 = high(case5, case6)
    numhigh4 = high(numhigh, numhigh2)
    result = high(numhigh3, numhigh4)
    print(result)

def high(num1, num2):
    """find high"""
    if num1 > num2:
        return num1
    return num2

main(input(), input(), input())
