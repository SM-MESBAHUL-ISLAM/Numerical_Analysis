import numpy as np
from matplotlib import pyplot as plt
import sympy as sy
import math

def Basis_Of_Simpson():
    equation = input("Enter the equation: ") #1/(1 + x**2)
    a, b = (map(float, input("Please Enter the lower limit(a) and upper limit(b): ").split(",")))

    f = lambda x: eval(equation)
    g = lambda x: (0 * x)

    def exact_solution(a, b):
        x = sy.Symbol("x")
        exact = sy.integrate(f(x), (x, a, b))
        return exact

    def basis_of_simpson(a, b):
        h = (b - a) / 2
        result = (h / 3) * (f(a) + (4 * f((a + b) / 2)) + f(b))
        return result

    ans = basis_of_simpson(a, b)
    exact_result = exact_solution(a, b)
    true_error = (exact_result - ans)
    true_percentage_error = (abs(true_error) / exact_result) * 100
    print("The result using Basis of Simpson's 1/3rd Rule : %.4f" %ans)
    print("The true percentage error : %.4f" %true_percentage_error)

# Basis_Of_Simpson()




