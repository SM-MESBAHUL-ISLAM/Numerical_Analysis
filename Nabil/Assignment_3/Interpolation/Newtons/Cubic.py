import sympy as sy

def Cubic_Interpolation(x_values,y_values,xf):

    xi = sy.Symbol("xi")
    xj = sy.Symbol("xj")
    yi = sy.Symbol("yi")
    yj = sy.Symbol("yj")
    F = lambda xi,xj,yi,yj : (yj-yi)/(xj-xi)

    for i in range(0, len(x_values)):
        if x_values[i] > xf:
            closePoint = i
            break

    x0 = x_values[closePoint-2]
    x1 = x_values[closePoint-1]
    x2 = x_values[closePoint]
    x3 = x_values[closePoint+1]

    y0 = y_values[closePoint-2]
    y1 = y_values[closePoint-1]
    y2 = y_values[closePoint]
    y3 = y_values[closePoint + 1]

    b0 = y0
    b1 = F(x0,x1,y0,y1)
    b2 = ( F(x1,x2,y1,y2) - b1 ) / (x2-x0)
    p1 = (F(x2,x3,y2,y3) -F(x1,x2,y1,y2)) / (x3-x1)

    p2 = (F(x1,x2,y1,y2) - b1)/ (x2 - x0)
    b3 = (p1 - p2) / (x3 - x0)

    result = b0 + (b1*(xf-x0)) + (b2* (xf-x0) *(xf-x1)) + (b3*(xf-x0)*(xf-x1)*(xf-x2))
    return result