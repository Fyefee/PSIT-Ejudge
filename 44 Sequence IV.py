"""Sequence IV"""
def main(num):
    """Sequence IV"""
    count = 1
    for _ in range(num):
        for _ in range(num):
            print(count, end=" ")
            count += 1
        print()

main(int(input()))
