import sympy as sy
def Cubic_Interpolation(x_list,y_list,xn):
    x = sy.Symbol("x")
    xi = sy.Symbol("xi")
    xj = sy.Symbol("xj")
    xk = sy.Symbol("xk")
    xl = sy.Symbol("xl")

    L = lambda x, xi, xj, xk,xl: ((x - xj) / (xi - xj)) * ((x - xk) / (xi - xk)) * ((x-xl)/(xi-xl))

    for i in range(0,len(x_list)):
        if x_list[i] > xn:
            nearbyPoint = i
            break
    x0 = x_list[nearbyPoint - 2]
    x1 = x_list[nearbyPoint - 1]
    x2 = x_list[nearbyPoint]
    x3 = x_list[nearbyPoint + 1]

    result = y_list[nearbyPoint-2]*L(xn,x0,x1,x2,x3) + y_list[nearbyPoint-1]*L(xn,x1,x0,x2,x3) + y_list[nearbyPoint]*L(xn,x2,x0,x1,x3) + y_list[nearbyPoint+1]*L(xn,x3,x0,x1,x2)
    return result

# Cubic_Interpolation()