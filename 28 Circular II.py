"""Circular II"""
def main(mex, mey, memos, friendx, friendy):
    """Circular II"""
    friendmos = float(input())
    distant = (((mex - friendx) ** 2) + ((mey - friendy) ** 2)) ** 0.5
    result = distant - memos - friendmos
    if result < 0:
        print("Yes")
    else:
        print("No")

main(float(input()), float(input()), float(input()), float(input()), float(input()))
