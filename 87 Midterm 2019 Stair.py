"""ig : chw_jeffy"""
def main(step, stair):
    """[Midterm 2019] Stair"""
    kao = 0
    count = 0
    for i in range(stair):
        nextstep = int(input())
        if nextstep > step:
            print("NO")
            return
        kao += nextstep
        if i == stair-1:
            if kao <= step:
                count += 1
            if kao > step:
                count += 2
        else:
            if kao < step:
                continue
            if kao == step:
                count += 1
                kao = 0
            if kao > step:
                kao = nextstep
                count += 1
    print(count)

main(int(input()), int(input()))
