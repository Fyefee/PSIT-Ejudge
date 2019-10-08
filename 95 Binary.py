"""ig : chw_jeffy"""
def main(num):
    """Binary"""
    result = ""
    while 1:
        result += str(num % 2)
        num //= 2
        if num == 1 or num == 0:
            if num == 1:
                result += str(num)
            break
    print(result[::-1])

main(int(input()))
