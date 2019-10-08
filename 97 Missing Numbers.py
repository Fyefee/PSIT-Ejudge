"""<3 Jeffy"""
def main(num_n):
    """Missing Numbers"""
    result = []
    while 1:
        num = int(input())
        if num == 0:
            break
        else:
            result.append(num)
    for i in range(1, num_n+1):
        if i not in result:
            print(i)

main(int(input()))
