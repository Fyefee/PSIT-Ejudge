"""Regulation"""
def main(numa, numb, text):
    """Regulation"""
    print("%30d"%numa)
    print("%030d"%numa)
    print("%.2f"%numb)
    print("%.12f"%numb)
    print("%40s"%text)

main(int(input()), float(input()), input())
