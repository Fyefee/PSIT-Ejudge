"""Gift III"""
def main(num):
    """Gift III"""
    high = 0
    result = 0
    for _ in range(num):
        weight = int(input())
        if weight > high:
            result = high
            high = weight
        elif weight < high and weight > result:
            result = weight
    if result == 0:
        print("Exit")
    else:
        print(result)
main(int(input()))
