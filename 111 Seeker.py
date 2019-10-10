"""ig : chw_jeffy"""
def main(text):
    """Seeker"""
    result = []
    num = ""
    for i in range(len(text)):
        if text[i].isdigit() == 1:
            num += text[i]
        if text[i].isdigit() == 0:
            result.append(num)
            num = ""
    result.append(num)
    for i in range(result.count("")):
        result.remove("")
    result = list(map(int, result))
    print(sum(result))

main(input())
