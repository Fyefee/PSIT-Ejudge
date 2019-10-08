"""ig : chw_jeffy"""
def main(text):
    """Run Length Dncoding"""
    num = ""
    for i in text:
        if i.isdigit() == 1:
            num += i
        elif i.isalpha() == 1:
            print(i*(int(num)), end="")
            num = ""

main(input())
