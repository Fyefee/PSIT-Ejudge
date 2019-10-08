"""Circular I"""
def main(mex, mey, hmos, mosx, mosy):
    """Circular I"""
    result = (((mex - mosx) ** 2) + ((mey - mosy) ** 2)) ** 0.5
    if result <= hmos and hmos != 0:
        print("Yes")
    else:
        print("No")

main(float(input()), float(input()), float(input()), float(input()), float(input()))
