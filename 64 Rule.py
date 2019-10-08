"""RuleofThree"""
def main(num):
    """RuleofThree"""
    high = 0
    pricehigh = 0
    weighthigh = 0
    for _ in range(num):
        price = float(input())
        weight = float(input())
        jeff = weight / price
        if jeff == high:
            if pricehigh >= price:
                pricehigh = price
                weighthigh = weight
        elif jeff > high:
            high = jeff
            pricehigh = price
            weighthigh = weight
    print("%.2f %.2f"%(pricehigh, weighthigh))
 
main(int(input()))