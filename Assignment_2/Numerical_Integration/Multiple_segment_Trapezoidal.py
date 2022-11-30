import math

import numpy as np
import sympy as sy
from matplotlib import  pyplot as plt

def Multiple_Segment_Trapezoidal_Rule():
    equation = input("Enter the equation: ")
    a, b = (map(float, input("Please Enter the lower limit(a) and upper limit(b): ").split(",")))
    n = int(input("Enter the number of Segment: "))

    # here is our equation
    # f = lambda x: 1/(1 + x**2)
    f = lambda x: eval(equation)
    g = lambda x: (0 * x)

    def exact_solution(a, b):
        x = sy.Symbol("x")
        exact = sy.integrate(f(x), (x, a, b))
        return exact

    def ans(a, b, h, n):
        p1 = ((b - a) * f(a)) / (2 * n)
        p2 = ((b - a) * f(b)) / (2 * n)
        sum = 0
        for i in range(1, n):
            sum += f(a + (i * h))
        result = p1 + ((b - a) * (sum / n)) + p2
        return result

    def multi_segment_rule(a, b, n):
        h = (b - a) / n
        result = ans(a, b, h, n)
        exact_result = exact_solution(a, b)
        true_error = (exact_result - result)
        true_percentage_error = (abs(true_error) / exact_result) * 100
        y = np.linspace(a, b + 2, 100)
        x = np.linspace(a, b, 100)
        plt.plot(y, f(y), label="upper_function")
        plt.plot(y, g(y), label="lower_function")
        plt.vlines(x=a, ymin=g(a), ymax=f(a))
        l = a
        for i in range(0, n - 1):
            l = l + h
            plt.plot([l - h, l], [f(l - h), f(l)])
            plt.vlines(x=l, ymin=g(l), ymax=f(l))
        plt.vlines(x=b, ymin=g(b), ymax=f(b))
        plt.plot([l, b], [f(l), f(b)])

        print("The ans from Multiple Segment Trapioidal Rule is : %.4f" % result)
        print("The True percenage error is : %.4f" % true_percentage_error, "%")
        plt.show()

    multi_segment_rule(a, b, n)

# Multiple_Segment_Trapezoidal_Rule()