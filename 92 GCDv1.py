"""ig : chw_jeffy"""
def main(num1, num2):
    """GCD_v1"""
    if num1 == 0 or num2 == 0:
        print(max(num1, num2))
    else:
        for i in range(min(num1, num2), 0, -1):
            if num1 % i == 0 and num2 % i == 0:
                print(i)
                break

main(int(input()), int(input()))
