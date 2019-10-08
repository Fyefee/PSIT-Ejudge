"""Indicator_Right"""
def main(yao, high):
    """Indicator_Right"""
    space = 0
    for _ in range(high//2+1):
        print(" "*space + "*"*yao)
        space += 1
    space -= 1
    for _ in range(high//2):
        space -= 1
        print(" "*space + "*"*yao)

main(int(input()), int(input()))
