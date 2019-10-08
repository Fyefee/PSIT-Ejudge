"""Bill"""
def main(num):
    """Bill"""
    service = num * 10 / 100
    if service < 50:
        service = 50
    if service > 1000:
        service = 1000
    nums = num + service
    vat = nums * 7 / 100
    result = nums + vat
    print("%.2f"%result)

main(int(input()))
