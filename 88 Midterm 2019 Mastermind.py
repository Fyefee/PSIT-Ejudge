"""ig : chw_jeffy"""
def main(answer, dao):
    """[Midterm 2019] Mastermind"""
    result_b = 0
    result_w = 0
    for i in range(4):
        if answer[i] == dao[i]:
            result_b += 1
    for i in set(dao):
        if i in answer:
            result_w += min(answer.count(i), dao.count(i))
    result_w -= result_b
    result_o = 4 - result_b - result_w
    print("B"*result_b + "W"*result_w + "O"*result_o)


main(list(input()), list(input()))
