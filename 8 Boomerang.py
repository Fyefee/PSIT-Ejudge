"""Boomerang"""
def main(numx, numy, numz):
    """Boomerang"""
    print(fun1(numx))
    print(fun2(numy))
    print(fun3(numz))
    print(fun4(numx, numy))
    print(fun5(numx, numy, numz))

def fun1(num):
    """eoeo"""
    return num + 1

def fun2(num):
    """eoeo"""
    return (7 * (num ** 3)) + (2 * (num ** 2)) - (31 * num) + 1

def fun3(num):
    """eoeo"""
    return num - num - num

def fun4(numx, numy):
    """eoeo"""
    return (numx + numy) * (numx - numy)

def fun5(numx, numy, numz):
    """eoeo"""
    return (numy - ((numy ** 2) - ((4 * numx * numz))) ** 0.5) / (2 * numx)

main(int(input()), int(input()), int(input()))
