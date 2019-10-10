"""ig : chw_jeffy"""
def main(num_n, num_m):
    """Difference"""
    result_a = []
    result_b = []
    result = []
    for _ in range(num_n):
        result_a.append(int(input()))
    for _ in range(num_m):
        result_b.append(int(input()))
    result = list(set(result_a) - set(result_b))
    result.sort()
    print(*result)


main(int(input()), int(input()))
