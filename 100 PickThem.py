"""<3 Jeffy"""
import json
def main(num):
    """PickThem"""
    result = json.loads(num)
    count = 0
    for i in result:
        if int(i) % 2 == 0:
            print(i)
            count += 1
    if count == 0:
        print("Nope")

main(input())
