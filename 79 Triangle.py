"""Triangle"""
def main(num):
    """Triangle"""
    print(" "*((num - 1) * 2) + "%02d"%num)
    count = 2
    for i in range(num-1, 0, -1):
        print(" "*((i - 1) * 2) + "%02d"%i + " "*count + "%02d"%i)
        count += 4

main(int(input()))
