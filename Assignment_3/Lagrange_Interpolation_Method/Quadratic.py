import sympy as sy
def Quadratic_Interpolation(x_list,y_list,xn):
    x = sy.Symbol("x")
    xi = sy.Symbol("xi")
    xj = sy.Symbol("xj")
    xk = sy.Symbol("xk")


    L = lambda x,xi,xj,xk: ((x - xj) / (xi - xj))*((x-xk)/(xi-xk))

    for i in range(0,len(x_list)):
        if x_list[i] > xn:
            nearbyPoint = i
            break
    x0 = x_list[nearbyPoint-2]
    x1 = x_list[nearbyPoint-1]
    x2 = x_list[nearbyPoint]
    result = y_list[nearbyPoint-2]*L(xn,x0,x1,x2) + y_list[nearbyPoint-1]*L(xn,x1,x0,x2) + y_list[nearbyPoint]*L(xn,x2,x0,x1)
    return result
# Quadratic_Interpolation()