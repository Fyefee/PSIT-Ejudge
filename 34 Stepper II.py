"""Stepper II"""
def main(num, num2):
    """Stepper II"""
    if num - num2 > 0:
        for i in range(num, num2-1, -1):
            print(i)
    else:
        for i in range(num, num2+1):
            print(i)

main(int(input()), int(input()))
