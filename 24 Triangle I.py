"""Triangle I"""
def main(num1, num2, num3):
    """Triangle I"""
    numhigh = num1
    numhigh2 = num2
    numhigh3 = num3
    if num1 > num2 and num1 > num3:
        numhigh = num1
        if num2 > num3:
            numhigh2 = num2
            numhigh3 = num3
        else:
            numhigh2 = num3
            numhigh3 = num2

    elif num2 > num1 and num2 > num3:
        numhigh = num2
        if num1 > num3:
            numhigh2 = num1
            numhigh3 = num3
        else:
            numhigh2 = num3
            numhigh3 = num1

    elif num3 > num2 and num3 > num1:
        numhigh = num3
        if num1 > num2:
            numhigh2 = num1
            numhigh3 = num2
        else:
            numhigh2 = num2
            numhigh3 = num1


    tmum = numhigh ** 2
    mum = (numhigh2 **2) + (numhigh3 ** 2)
    result = int((tmum - mum) * 100)

    if result == 0:
        print("Yes")
    else:
        print("No")

main(float(input()), float(input()), float(input()))

