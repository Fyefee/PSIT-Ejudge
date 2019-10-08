"""EiEI"""
def main():
    """Restaurant"""
    abath = float(input())
    bbath = float(input())
    pro = float(input())
    exp = float(input())
    result = (abath + exp) - (((abath + exp) * pro) / 100)
    result2 = abath - (abath * pro / 100)
    if abath == result or result == result2:
        print("Yes")
    elif bbath == abath:
        print("No %.3f"%(result - result2))
    elif result > abath:
        print("No %.3f"%(result - abath))
    elif result < abath:
        print("Yes %.3f"%(abath - result))
main()
