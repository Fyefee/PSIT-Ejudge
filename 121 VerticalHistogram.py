"""ig : chw_jeffy"""
def main(text):
    """VerticalHistogram"""
    resultnum = []
    result = list(set(text))
    result.sort(key=str.swapcase)
    for j in range(len(result)):
        count = text.count(result[j])
        resultnum.append(count)
    resultnump = resultnum.copy()
    resultnump.sort()
    high = len(resultnump) - 1
    if len(result) != 0:
        for k in range(resultnump[high], 0, -1):
            print("%03d"%k, end="")
            for lll in range(len(resultnum)):
                if str(k) in str(resultnum[lll]):
                    print(" *", end="")
                    resultnum[lll] = k - 1
                else:
                    print("  ", end="")
            print("")
        print("   ", *result)

main(input())
