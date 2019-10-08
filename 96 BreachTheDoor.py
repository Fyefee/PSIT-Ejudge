"""<3 Jeffy"""
def main(text):
    """BreachTheDoor"""
    text = text.split(" ")
    for i in text:
        result = ""
        for j in i:
            if j.isalpha() == 1:
                result += j
        if len(result) > 6:
            print(result, end=" ")

main(input())
