"""<3 Jeffy"""
def main(text):
    """FOR!F-Ball"""
    result = 1
    for i in text:
        if i == "A":
            if result == 1:
                result = 2
            elif result == 2:
                result = 1
        elif i == "B":
            if result == 2:
                result = 3
            elif result == 3:
                result = 2
        elif i == "C":
            if result == 1:
                result = 3
            elif result == 3:
                result = 1
    print(result)
main(input())
