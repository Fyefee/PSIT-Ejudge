"""Sequence I"""
def main(num):
    """Sequence I"""
    for _ in range(1, num+1):
        for j in range(1, num+1):
            print(j, end=" ")
        print()

main(int(input()))
