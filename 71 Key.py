"""<3 Jeffy"""
def main(num):
    """Key"""
    result = 0
    for i in num:
        result += int(i)
    position = len(str(num))
    result2 = int(num[position-3:]) * 10
    result3 = result + result2
    if len(str(result3)) > 4:
        result4 = str(result3)[len(str(result3))-4:]
        print(result4)
    elif result3 < 1000:
        result3 += 1000
        print(result3)
    else:
        print(result3)

main(input())
