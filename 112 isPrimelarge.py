"""ig : chw_jeffy"""
def main(num):
    """isprime_large"""
    count = 0
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            count += 1
    if count > 0 or num == 0 or num == 1:
        print("NO")
    else:
        print("YES")

main(int(input()))
