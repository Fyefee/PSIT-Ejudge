"""Sequence X"""
def main(num):
    """Sequence X"""
    for i in range(1, num):
        for j in range(-num+1, num):
            if abs(j) < i:
                print("%02d"%(i-abs(j)), sep="", end=" ")
            else:
                print("  ", end=" ")
        print()
    for i in range(num, 0, -1):
        for j in range(-num+1, num):
            if abs(j) < i:
                print("%02d"%(i-abs(j)), sep="", end=" ")
            else:
                print("  ", end=" ")
        print()

main(int(input()))
