"""ig : chw_jeffy"""
def main(num1, num2):
    """Duplicate I"""
    mem1 = []
    mem2 = []
    result = []
    for _ in range(num1):
        mem1.append(input())
    for _ in range(num2):
        mem2.append(input())
    for i in mem2:
        if i in mem1:
            result.append(i)
    result.sort(reverse=True)
    if len(result) == 0:
        print("Nope")
    else:
        print(*result, sep="\n")

main(int(input()), int(input()))
