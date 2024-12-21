import math

class NumberCalculator:
    def __init__(self):
        pass

    def calculate_result(self, n):
        return n * (n + 1) // 2 - 2 * (2 ** (int(math.log2(n)) + 1) - 1)

if __name__ == "__main__":
    number_calculator = NumberCalculator()
    test_cases = int(input())

    for i in range(test_cases):
        n = int(input())
        result = number_calculator.calculate_result(n)
        print(result)
