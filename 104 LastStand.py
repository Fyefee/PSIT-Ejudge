"""ig : chw_jeffy"""
import json
def main(text):
    """Seeker"""
    result = json.loads(text)
    result = list(map(str, result))
    for i in result:
        print(i[len(i)-1])

main(input())
