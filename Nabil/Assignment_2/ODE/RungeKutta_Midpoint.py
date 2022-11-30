import numpy as np
import matplotlib.pyplot as plt
import math

def RungeKutta_MidpointMethod():
    xi,yi,xn = (map(float,input("Please Enter x(initial),y(initial) and x(final) : ").split(",")))
    Total_number_of_stepSize = int(input("Enter the number of step size: "))
    h = []
    print("Enter the step sizes: ")
    for i in range(0,Total_number_of_stepSize):
        h.append(float(input()))

    dydx = lambda x, y: 2*y
    f = lambda x: math.exp(2*x)

    def drawCurve(xi, xn):
        x_axisPoints = np.linspace(xi, xn, 150)
        y_axisPoints = np.exp(2 * x_axisPoints)
        plt.plot(x_axisPoints, y_axisPoints, label="Actual Curve")

    def MidpointMethod(xi, yi, xn, h, total_stepsize):
        drawCurve(xi, xn)

        for i in range(0, total_stepsize):
            print("When Step Size, h= " + f'{h[i]:.3f}' + "\n")
            steps_need = int((xn - xi) / h[i])
            cur_x = xi
            cur_y = yi
            x_points = []
            y_points = []
            print(" \t X \t\t  Y ")

            for j in range(0, steps_need):
                print(f'{cur_x:.3f}' + "\t\t" + f'{cur_y:.3f}' + "\n")
                x_points.append(cur_x)
                y_points.append(cur_y)
                k1 = dydx(cur_x, cur_y)
                k2 = dydx(cur_x + h[i] / 2, cur_y + (k1 * h[i]) / 2)
                cur_y = cur_y + (k2 * h[i])
                cur_x = h[i] + cur_x

            print(f'{cur_x:.3f}' + "\t\t" + f'{cur_y:.3f}' + "\n")
            x_points.append(cur_x)
            y_points.append(cur_y)
            actual_error = abs((f(xn) - cur_y) / f(xn))
            actual_error = actual_error * 100

            plt.plot(x_points, y_points, label="Step size: {} & Error: {}".format(h[i], f'{actual_error:.3f}'))
            print("Answer using h= " + f'{h[i]:.3f}' + " =" + f'{cur_y:.3f}' + "\n")
            print("True percentage error : " f'{actual_error:.3f}')
            x_points.clear()
            y_points.clear()

        plt.legend()
        plt.show()
    MidpointMethod(xi,yi,xn,h,Total_number_of_stepSize)