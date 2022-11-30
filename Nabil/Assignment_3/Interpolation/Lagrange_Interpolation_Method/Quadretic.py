import sympy as sy


def Quadratic_Interpolation(x_values,y_values,xf):
    x = sy.Symbol("x")
    xi = sy.Symbol("xi")
    xj = sy.Symbol("xj")
    xk = sy.Symbol("xk")


    L = lambda x,xi,xj,xk: ((x - xj) / (xi - xj))*((x-xk)/(xi-xk))

    for i in range(0,len(x_values)):
        if x_values[i] > xf:
            closePoint = i
            break
    x0 = x_values[closePoint-2]
    x1 = x_values[closePoint-1]
    x2 = x_values[closePoint]
    result = y_values[closePoint-2]*L(xf,x0,x1,x2) + y_values[closePoint-1]*L(xf,x1,x0,x2) + y_values[closePoint]*L(xf,x2,x0,x1)
    return result
