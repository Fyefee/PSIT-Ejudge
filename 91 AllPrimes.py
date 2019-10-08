"""ig : chw_jeffy"""
def main(num):
    """All_Primes"""
    result = 0
    for i in range(1, num+1):
        if check(i) == 1:
            result += 1
    print(result)

def check(num):
    """isprime_small"""
    count = 0
    for i in range(2, num//2+1):
        if num % i == 0:
            count += 1
    if count > 0 or num == 0 or num == 1:
        return 0
    else:
        return 1

main(int(input()))
