"""ig : chw_jeffy"""
def main():
    """[Midterm 2019] Lotto"""
    price1 = input()
    price2 = input()
    price3f1 = input()
    price3f2 = input()
    price3b1 = input()
    price3b2 = input()
    mynum = input()
    result = 0
    if price1 == mynum:
        result += 6000000
    if price1 == "000000" and (mynum == "999999" or mynum == "000001"):
        result += 100000
    elif price1 == "999999" and (mynum == "999998" or mynum == "000000"):
        result += 100000
    elif int(mynum) in range(int(price1)-1, int(price1)+2) and mynum != price1:
        result += 100000
    if mynum[:3:] == price3f1:
        result += 4000
    if mynum[:3:] == price3f2:
        result += 4000
    if mynum[3::] == price3b1:
        result += 4000
    if mynum[3::] == price3b2:
        result += 4000
    if mynum[4:] == price2:
        result += 2000
    print(result)

main()
