import sympy as sy

def Quadratic_Interpolation(x_values,y_values,xf):

    xi = sy.Symbol("xi")
    xj = sy.Symbol("xj")
    yi = sy.Symbol("yi")
    yj = sy.Symbol("yj")
    F = lambda xi,xj,yi,yj : (yj-yi)/(xj-xi)

    for i in range(0, len(x_values)):
        if x_values[i] > xf:
            closePoint = i
            break

    x0 = x_values[closePoint-1]
    x1 = x_values[closePoint]
    x2 = x_values[closePoint+1]

    y0 = y_values[closePoint - 1]
    y1 = y_values[closePoint]
    y2 = y_values[closePoint + 1]

    b0 = y0
    b1 = F(x0,x1,y0,y1)
    b2= ( F(x1,x2,y1,y2) - b1 ) / (x2-x0)

    result = b0 + (b1*(xf-x0)) + (b2* (xf-x0) *(xf-x1))
    return result