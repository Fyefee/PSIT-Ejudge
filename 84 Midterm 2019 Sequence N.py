"""ig : chw_jeffy"""
def main(size):
    """[Midterm 2019] Sequence N"""
    space_left = 0
    space_right = size - 3
    print("*" + " "*(size-2) + "*")
    for _ in range(size-2):
        print("*" + " "*space_left + "*" + " "*space_right + "*")
        space_left += 1
        space_right -= 1
    print("*" + " "*(size-2) + "*")

main(int(input()))
