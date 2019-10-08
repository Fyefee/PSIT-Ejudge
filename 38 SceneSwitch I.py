"""SceneSwitch"""
def main(time):
    """SceneSwitch"""
    last, count, mode, status = 0, 0, 0, 0
    while time != "End":
        time = float(time)
        status = (status + 1) % 2
        if status:
            if time - last > 6:
                mode = 0
            count += mode
            mode = (mode + 1) % 2
        last = time
        time = input()
    print(count)

main(input())
