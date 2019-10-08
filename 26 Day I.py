"""Day I"""
def main(year):
    """Day I"""
    if year % 4 == 0:
        if year % 100 != 0:
            print("Yes")
        elif year % 100 == 0 and year % 400 == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
main(int(input()))
