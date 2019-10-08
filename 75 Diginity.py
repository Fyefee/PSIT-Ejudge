"""<3 Jeffy"""
def main():
    """Diginity_Midterm2014"""
    while 1:
        num = int(input())
        score = 0
        if num == 0:
            break
        for i in str(num):
            score += int(i)
            num = score
        while len(str(num)) != 1:
            score = 0
            for i in str(num):
                score += int(i)
            num = score
        print(num)

main()
