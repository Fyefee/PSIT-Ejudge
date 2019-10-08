"""Sequence II"""
def main(num, num_start, num_plus):
    """Sequence II"""
    for _ in range(num):
        print(num_start, end=" ")
        num_start += num_plus
        num_plus += 2

main(int(input()), 1, 3)
