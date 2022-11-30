import numpy as np
import sympy as sy
from matplotlib import pyplot as plt



def Single_Segment_Trapezoidal():
    equation = input("Enter the equation: ")
    a, b = (map(float, input("Please Enter the lower limit(a) and upper limit(b): ").split(",")))

    # f = lambda x: (2*(x**2) + 3*x + 5)
    f = lambda x: eval(equation)
    g = lambda x: (0 * x)
    # line = lambda x,a,b: (((x-a)*((f(a)-f(b))/(a-b))) + f(a))
    I = lambda a, b: (b - a) * ((f(a) + f(b)) / 2)

    def exact_solution(a, b):
        x = sy.Symbol("x")
        exact = sy.integrate(f(x), (x, a, b))
        return exact

    def Single_segment_rule(a, b):
        ans = I(a, b)
        exact_result = exact_solution(a, b)
        true_error = (exact_result - ans)
        true_percentage_error = (abs(true_error) / exact_result) * 100
        y = np.linspace(a, b + 2, 100)
        x = np.linspace(a, b, 100)
        plt.plot(y, f(y), label="upper_function")
        plt.plot(y, g(y), label="lower_function")

        plt.vlines(x=a, ymin=g(a), ymax=f(a))
        plt.vlines(x=b, ymin=g(b), ymax=f(b))
        plt.plot([a, b], [f(a), f(b)])
        plt.fill_between([a, b], [f(a), f(b)], color='lightgreen', label='Area using Trapezoidal Rule')
        # plt.plot(x,line(x,a,b))
        # plt.fill_between(x,g(x),line(x,a,b),color='lightgreen',label='trapizoid')
        # plt.fill_between(x,f(x),g(x),label = "area")
        plt.legend()
        print("The ans from Single Segment Trapioidal Rule is : %.4f" % ans)
        print("The True percenage error is : %.4f" % true_percentage_error, "%")
        plt.show()

    Single_segment_rule(a,b)


# Single_Segment_Trapezoidal()