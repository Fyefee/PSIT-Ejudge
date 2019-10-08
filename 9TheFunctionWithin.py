"""TheFunctionWithin"""
def mainfunction():
    """main"""
    num_a = float(input())
    num_b = float(input())
    num_c = float(input())
    num_d = float(input())
    ans_1 = function_f(function_f(num_a))
    ans_2 = function_g(function_f(num_a-num_b))
    ans_3 = function_h(function_f(num_a+num_b), function_f(num_a+num_c), \
            function_g(function_f(num_d**2)))
    ans_4 = function_i(function_h(function_f(num_a+num_b), \
            function_f(num_a-num_c), function_g(function_f(num_d**2))), \
            function_g(function_f(num_a-num_b)), \
            function_f(function_f(function_f(function_f(function_f(num_c))))), num_d**8)
    print(ans_1)
    print(ans_2)
    print(ans_3)
    print(ans_4)

def function_f(num_x):
    """func_f"""
    return 2*num_x

def function_g(num_x):
    """func_g"""
    return 3*(num_x**4)-(num_x**3)+2*(num_x**2)+10

def function_h(num_x, num_y, num_z):
    """func_h"""
    return ((num_z+num_x)**2)-num_x*num_y+(num_y**2)

def function_i(num_a, num_b, num_c, num_d):
    """func_i"""
    return ((num_a**2)+(num_b**2)-(num_c**2))/((num_d**2)-(2*num_a*num_d)+2*num_a)

mainfunction()
