"""Divide3Or5"""
def main(num):
    """Divide3Or5"""
    result = 0
    for i in range(1, num+1):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    print(result)

main(int(input()))
