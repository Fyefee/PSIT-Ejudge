"""ig : chw_jeffy"""
import json
def main(score, filter_score):
    """Filter"""
    result = []
    for i in score:
        if score[i] >= filter_score:
            result.append(i)
    result.sort()
    if len(result) > 0:
        for i in result:
            print("%s\t%.2f"%(i, score[i]))
    else:
        print("Nope")

main(json.loads(input()), float(input()))
