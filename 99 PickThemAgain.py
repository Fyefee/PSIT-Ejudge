"""<3 Jeffy"""
def main(num):
    """PickThemAgain"""
    num = num.split(" ")
    count = 0
    for i in num[::-1]:
        if int(i) % 3 == 0 or int(i) % 5 == 0:
            print(i)
            count += 1
    if count == 0:
        print("Nope")

main(input())
