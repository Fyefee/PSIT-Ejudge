"""ig: chw_jeffy"""
def main(num):
    """AlmostMean"""
    student_dict = {}
    student_score = []
    high = 0
    for _ in range(num):
        student = input()
        student_dict[float(student[9:])] = student[0:8]
        student_score.append(float(student[9:]))
    score_mean = sum(student_score) / num
    for i in student_score:
        if i <= score_mean and i >= high:
            high = i
    print("%s\t%s"%(student_dict[high], high))

main(int(input()))
