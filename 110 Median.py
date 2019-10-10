"""ig : chw_jeffy"""
def main(num):
    """Median"""
    result = []
    for _ in range(num):
        result.append(float(input()))
    result.sort()
    if num % 2 != 0:
        print("%.01f"%result[num//2])
    else:
        print("%.01f"%((result[num//2-1] + result[num//2]) / 2))

main(int(input()))
