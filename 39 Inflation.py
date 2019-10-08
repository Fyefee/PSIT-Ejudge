"""Inflation"""
def main(money, year):
    """Inflation"""
    money = int(money * 100)
    for _ in range(year):
        money += int(money * 381) // 10000
    result1 = money // 100
    result2 = money % 100
    print("%d.%02d" %(result1, result2))

main(float(input()), int(input()))
