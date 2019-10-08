"""DataSpike"""
def main():
    """main"""
    data_1 = int(input())
    data_2 = int(input())
    data_3 = int(input())
    data_4 = int(input())
    data_5 = int(input())
    data_6 = int(input())
    data_7 = int(input())
    data_8 = int(input())
    data_highest = 0
    data_highest = function_check(data_1, data_2)
    data_highest = function_check(data_highest, data_3)
    data_highest = function_check(data_highest, data_4)
    data_highest = function_check(data_highest, data_5)
    data_highest = function_check(data_highest, data_6)
    data_highest = function_check(data_highest, data_7)
    data_highest = function_check(data_highest, data_8)
    print(data_highest)

def function_check(data_a, data_b):
    """check"""
    if data_a > data_b:
        return data_a
    else:
        return data_b

main()
