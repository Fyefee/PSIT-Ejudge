"""ig : chw_jeffy"""
def main(coin):
    """CoinChangev1"""
    result = 0
    result += coin // 25
    coin %= 25
    result += coin // 10
    coin %= 10
    result += coin // 5
    coin %= 5
    result += coin // 1
    print(result)

main(int(input()))
