"""ig : chw_jeffy"""
def main():
    """[Midterm 2019] Harshad Number"""
    for _ in range(10):
        num = input().replace("-", "")
        num2 = 0
        for i in num:
            num2 += int(i)
        if num == "0":
            print("No")
        elif int(num) % num2 == 0:
            print("Yes")
        else:
            print("No")

main()
