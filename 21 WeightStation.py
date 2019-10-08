"""WeightStation"""
def main(weight, wheel_1, wheel_2, wheel_3):
    """WeightStation"""
    allweight = wheel_1 + wheel_2 + wheel_3
    wheel_4 = (weight * 4) - allweight
    result = wheel_1 + wheel_2 + wheel_3 + wheel_4
    weight2 = weight / 2
    if result > 15000:
        print("Overweight")
    elif wheel_1 < weight2 or wheel_2 < weight2 or wheel_3 < weight2 or wheel_4 < weight2:
        print("Unbalance")
    else:
        print("Pass %.2f"%wheel_4)

main(float(input()), float(input()), float(input()), float(input()))
