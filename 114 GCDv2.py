"""ig : chw_jeffy"""
def main(num1, num2):
    """GCD_v2"""
    if num1 < num2:
        num1, num2 = num2, num1
    while num2 > 0:
        result = num2
        num2 = num1 % num2
        num1 = result
    print(num1)

main(abs(int(input())), abs(int(input())))
