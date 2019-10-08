"""ig : chw_jeffy"""
def main(allday):
    """HappyDay"""
    count = 0
    allday = list(map(int, allday))
    past = max(allday)
    for i in allday:
        if i >= 80 or (i >= 20 and i - past >= 10):
            count += 1
        past = i
    print(count)

main(input().split(","))
