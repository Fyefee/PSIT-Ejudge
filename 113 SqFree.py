"""ig : chw_jeffy"""
def main(num):
    """SqFree"""
    count = 0
    check = 0
    for i in range(1, num+1):
        for j in range(2, int(i**0.5)+1):
            if i % (j ** 2) == 0:
                check += 1
                break
        if check == 0:
            count += 1
            check = 0
        else:
            check = 0
    print(count)

main(int(input()))
