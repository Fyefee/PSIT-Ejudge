"""<3 Jeffy"""
def main(alice, bob, car):
    """Nearer"""
    nearalice = abs(car - alice)
    nearbob = abs(car - bob)
    if nearalice == nearbob:
        print("Sundaes %d"%nearalice)
    elif nearalice > nearbob:
        print("Bob %d"%(nearbob))
    else:
        print("Alice %d"%(nearalice))

main(int(input()), int(input()), int(input()))
