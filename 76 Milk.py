"""IG : chw.jeffy"""
def main(price, promotion, plus, money):
    """Milk"""
    milk = money // price
    cap = milk
    while cap >= promotion and promotion != 0:
        capplus = (cap//promotion) * plus
        cap %= promotion
        cap += capplus
        milk += capplus
    print(milk)

main(int(input()), int(input()), int(input()), int(input()))
