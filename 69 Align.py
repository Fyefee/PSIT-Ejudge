"""<3 Jeffy"""
def main(yao, position, text):
    """Align"""
    if position.lower() == "right":
        print('{:>{}}'.format(text, yao))
    elif position.lower() == "left":
        print('{:<{}}'.format(text, yao))
    elif position.lower() == "center" and (yao - len(text)) % 2 != 0:
        print(" " + '{:^{}}'.format(text, yao))
    else:
        print('{:^{}}'.format(text, yao))
main(int(input()), input(), input())
