"""Sequence XI"""
def main(num):
    """Sequence XI"""
    for i in range(-num+1, num):
        for j in range(-num+1, num):
            print("%02d"%(num - max(abs(i), abs(j))), sep="", end=" ")
        print()

main(int(input()))
