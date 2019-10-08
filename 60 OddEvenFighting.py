"""OddEvenFighting"""
def main():
    """OddEvenFighting"""
    nume = 0
    numo = 0
    while 1:
        num = int(input())
        if num == 0:
            break
        if num % 2 == 0:
            nume += num
        else:
            numo += num
    if nume > numo:
        print("Even %d"%nume)
    elif numo > nume:
        print("Odd %d"%numo)
    elif numo == nume:
        print("Draw %d"%nume)

main()
