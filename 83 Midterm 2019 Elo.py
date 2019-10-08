"""<3 Jeffy"""
def main(num_ra, num_rb, aorb):
    """[Midterm 2019] Elo"""
    _ = [print("%.2f"%(1/(1 + 10 ** ((num_rb - num_ra) / 400)))) if aorb == "A" else \
        print("%.2f"%(1/(1 + 10 ** ((num_ra - num_rb) / 400))))]


main(int(input()), int(input()), input())
