"""ig : chw_jeffy"""
def main(text):
    """HorizontalHistogram"""
    result = list(text)
    allchr = list(set(result))
    allchr.sort(key=str.swapcase)

    for i in allchr:
        print("%s : "%i, end="")
        if result.count(i) % 5 == 0:
            print("-----|"*(result.count(i)//5-1) + "-----")
        else:
            print("-----|"*(result.count(i)//5) + "-"*(result.count(i)%5))

main(input())
