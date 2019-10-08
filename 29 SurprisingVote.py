"""SurprisingVote"""
def main(num1, num2):
    """SurprisingVote"""
    score = num1 - num2 - num2
    if num2 - (score + 2) > 0 and num1 - num2 > 2:
        print("Surprising")
    elif num2 - ((num1 - num2) // 2) > 2:
        print("Surprising")
    else:
        print("Not surprising")

main(float(input()), float(input()))
