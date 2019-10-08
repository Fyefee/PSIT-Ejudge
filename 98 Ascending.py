"""<3 Jeffy"""
def main():
    """Ascending"""
    result = []
    for _ in range(5):
        num = int(input())
        result.append(num)
    result.sort()
    print(*result, sep="\n")

main()
