"""Sequence VIII"""
def main(num):
    """Sequence VIII"""
    space = (num - 1) * 3
    for i in range(1, num+1):
        print(" "*space, end="")
        for j in range(1, i+1):
            print("%02d"%j, end=" ")
        space -= 3
        print()

main(int(input()))
