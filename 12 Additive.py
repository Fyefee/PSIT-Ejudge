"""Additive"""
import math as m
def main():
    """Additive"""
    result1 = (m.sin(m.radians(90)) + (m.sin(m.radians(60))**2)) \
        / (m.cos(m.radians(245 ** 2)) + m.cos(m.radians(45 + 135)))
    result2 = (m.factorial(16) * m.factorial(4))/(m.factorial(8))
    result3 = (15 + 25) / (m.sqrt((25-12) ** 2 + (12-15) ** 2))
    result4 = m.log10(1234**4)
    result5 = (m.log(4234, 5) + m.log(8191, 2) + (71 * m.log10(156154))) \
        / (m.log(777, 7) - m.log(888, 8) - m.log(999, 9))

    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)

main()
