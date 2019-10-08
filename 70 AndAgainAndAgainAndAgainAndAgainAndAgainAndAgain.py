"""<3 Jeffy"""
def main(text):
    """AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
    alp = "aeiou"
    text = text.replace(".", "")
    text = text.split()
    result = []
    for i in range(len(text)):
        count = 0
        for j in text[i]:
            if j in alp:
                count += 1
        if count >= 2:
            result.append(text[i])
    result = sorted(result)
    if len(result) > 0:
        print(*result, sep="\n")
    else:
        print("Nope")

main(input())
