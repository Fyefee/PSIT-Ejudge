"""ig : chw_jeffy"""
def main(text):
    """LetterFrequency"""
    high = 0
    for i in set(text):
        if text.count(i) > high and i.isalpha() == 1:
            high = text.count(i)
            highchr = i
    print(highchr)

main(list(input().lower()))
