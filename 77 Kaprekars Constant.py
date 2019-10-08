"""IG : chw.jeffy"""
def main(num):
    """Kaprekar's Constant"""
    count = 0
    while num != "6174":
        highest = ""
        num = "%04d"%int(num)
        for i in range(9, -1, -1):
            if str(i) in num:
                highest += str(i) * num.count(str(i))
        num = str(int(highest) - int(highest[::-1]))
        count += 1
    print(count)

main(input())
