"""ClockHandsTouch"""
def main(hour, minn):
    """ClockHandsTouch"""
    if hour > 12:
        hour -= 12
    yao = (hour * 30) + (minn * 0.5)
    san = minn * 6
    if int(yao) in range(san, san+7):
        print("True")
    else:
        print("False")

main(int(input()), int(input()))
