"""Sequence IX"""
def main(num):
    """Sequence IX"""
    for i in range(1, num+1):
        for j in range(-num+1, num+1):
            if abs(j) < i:
                print("%02d"%(i-abs(j)), sep="", end=" ")
            else:
                print("  ", end=" ")
        print()

main(int(input()))
