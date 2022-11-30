import math
import matplotlib.pyplot as plt
import numpy as np

def Euler_Method():
    xi,yi,xf = (map(float,input("Please Enter x(initial),y(initial) and x(final) : ").split(",")))
    number_of_step_sizes = int(input("Enter the number of step size: "))
    h = []
    print("Enter the step sizes: ")
    for i in range(0,number_of_step_sizes):
        h.append(float(input()))

    dy = lambda x, y: (2 * y)  # dy/dx = 2*(e^2x) = 2*y
    f = lambda x: math.exp(2 * x)  # y = e^(2x)

    def analytical_curve(xi, xf):
        a = np.linspace(xi, xf, 100)
        y = np.exp(2 * a)
        plt.plot(a, y, label="Analytical")

    def euler(xi, yi, xf, h, num_of_stepSize):  # (initial x0 and y0, h-> step size)

        analytical_curve(xi, xf)
        for i in range(num_of_stepSize):
            n = int((xf - xi) / h[i])
            x = xi
            y = yi
            print("For step size h = %.3f: " % h[i])
            print('\tx  \t\t\t y')
            print('%f \t %f' % (x, y))
            x_plot = []
            euler = []
            exact_ans = f(xf)
            for j in range(0, n):
                x_plot.append(x);
                euler.append(y)
                y = y + dy(x, y) * h[i]
                x = x + h[i]
                print('%f \t %f' % (x, y))
            x_plot.append(x);
            euler.append(y)
            plt.plot(x_plot, euler, label="Step_size = %.3f" % h[i])
            x_plot.clear()
            euler.clear()
            error = (abs(exact_ans - y) / exact_ans) * 100
            print("The ans is y = ", y, " And the true percentage Error = %f" % error, "%")
            print("\n")
        plt.legend()
        plt.show()

    euler(xi,yi,xf,h,number_of_step_sizes)

