"""ig : chw_jeffy"""
def main(num):
    """LineSorting"""
    result = []
    for _ in range(num):
        result.append(input())
    result.sort(key=len)
    print(*result, sep="\n")

main(int(input()))
