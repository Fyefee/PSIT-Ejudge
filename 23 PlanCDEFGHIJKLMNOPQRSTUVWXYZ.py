"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def main(text, num1, num2, num3):
    """PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
    numhigh = num1
    numhigh2 = num2
    numhigh3 = num3
    if num1 >= num2 and num1 >= num3:
        numhigh = num1
        if num2 > num3:
            numhigh2 = num2
            numhigh3 = num3
        else:
            numhigh2 = num3
            numhigh3 = num2

    elif num2 >= num1 and num2 >= num3:
        numhigh = num2
        if num1 > num3:
            numhigh2 = num1
            numhigh3 = num3
        else:
            numhigh2 = num3
            numhigh3 = num1

    elif num3 >= num2 and num3 >= num1:
        numhigh = num3
        if num1 > num2:
            numhigh2 = num1
            numhigh3 = num2
        else:
            numhigh2 = num2
            numhigh3 = num1

    if text == "Descend":
        print("%.2f, %.2f, %.2f"%(numhigh, numhigh2, numhigh3))

    if text == "Ascend":
        print("%.2f, %.2f, %.2f"%(numhigh3, numhigh2, numhigh))

main(input(), float(input()), float(input()), float(input()))
