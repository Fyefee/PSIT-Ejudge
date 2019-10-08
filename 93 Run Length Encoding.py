"""ig : chw_jeffy"""
def main(text):
    """Run Length Encoding"""
    count = 0
    countalpha = 0
    alpha = text[count]
    while count != len(text):
        if text[count] == alpha:
            count += 1
            countalpha += 1
        else:
            print(str(countalpha) + alpha, end="")
            countalpha = 0
            alpha = text[count]
    print(str(countalpha) + alpha, end="")

main(input())
