"""Sequence V"""
def main(num):
    """Sequence V"""
    count = 0
    for _ in range(num):
        if count == 7:
            print()
            count = 0
        print(num, end=" ")
        num -= 1
        count += 1

main(int(input()))
