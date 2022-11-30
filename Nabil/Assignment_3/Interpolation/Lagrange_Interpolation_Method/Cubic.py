import sympy as sy


def Cubic_Interpolation(x_values,y_values,xf):
    x = sy.Symbol("x")
    xi = sy.Symbol("xi")
    xj = sy.Symbol("xj")
    xk = sy.Symbol("xk")
    xl = sy.Symbol("xl")

    L = lambda x, xi, xj, xk,xl: ((x - xj) / (xi - xj)) * ((x - xk) / (xi - xk)) * ((x-xl)/(xi-xl))

    for i in range(0,len(x_values)):
        if x_values[i] > xf:
            closePoint = i
            break
    x0 = x_values[closePoint - 2]
    x1 = x_values[closePoint - 1]
    x2 = x_values[closePoint]
    x3 = x_values[closePoint + 1]

    result = y_values[closePoint-2]*L(xf,x0,x1,x2,x3) + y_values[closePoint-1]*L(xf,x1,x0,x2,x3) + y_values[closePoint]*L(xf,x2,x0,x1,x3) + y_values[closePoint+1]*L(xf,x3,x0,x1,x2)
    return result
