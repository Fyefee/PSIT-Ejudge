"""<3 Jeffy"""
def main(left, right):
    """Hamburger"""
    print("|"*left + "*"*((left + right) * 2) + "|"*right)

main(int(input()), int(input()))
