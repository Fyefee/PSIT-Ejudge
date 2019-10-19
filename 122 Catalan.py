"""ig : chw_jeffy"""
def main(num_n):
    """Catalan"""
    result = 1
    for i in range(2, num_n+1):
        result = (4 * (i-1) + 2) / ((i-1) + 2) * result
    print(int(result))

main(int(input()))
