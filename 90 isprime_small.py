"""ig : chw_jeffy"""
def main(num):
    """isprime_small"""
    count = 0
    for i in range(2, num//2+1):
        if num % i == 0:
            count += 1
    if count > 0 or num == 0 or num == 1:
        print("No")
    else:
        print("Yes")

main(int(input()))
