"""Grade III"""
def main(num):
    """Grade III"""
    grade = 0
    for _ in range(num):
        score = float(input())
        if score <= 100 and score >= 95:
            grade += 4
        elif score < 95  and score >= 90:
            grade += 3.5
        elif score < 90 and score >= 85:
            grade += 3
        elif score < 85 and score >= 80:
            grade += 2.5
        elif score < 80 and score >= 75:
            grade += 2
        elif score < 75 and score >= 70:
            grade += 1.5
        elif score < 70 and score >= 65:
            grade += 1
        elif score < 65 and score >= 60:
            grade += 0.5
        elif score < 60 and score >= 0:
            grade += 0
    result = (int((grade / num) * 100)) / 100
    print("%.2f"%result)

main(int(input()))
