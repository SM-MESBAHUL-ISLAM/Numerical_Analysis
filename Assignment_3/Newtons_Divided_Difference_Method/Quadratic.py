import sympy as sy

def Quadratic_Interpolation(x_list,y_list,xn):

    xi = sy.Symbol("xi")
    xj = sy.Symbol("xj")
    yi = sy.Symbol("yi")
    yj = sy.Symbol("yj")
    F = lambda xi,xj,yi,yj : (yj-yi)/(xj-xi)

    for i in range(0, len(x_list)):
        if x_list[i] > xn:
            nearbyPoint = i
            break

    x0 = x_list[nearbyPoint-1]
    x1 = x_list[nearbyPoint]
    x2 = x_list[nearbyPoint+1]

    y0 = y_list[nearbyPoint - 1]
    y1 = y_list[nearbyPoint]
    y2 = y_list[nearbyPoint + 1]

    b0 = y0
    b1 = F(x0,x1,y0,y1)
    b2= ( F(x1,x2,y1,y2) - b1 ) / (x2-x0)

    yn = b0 + (b1*(xn-x0)) + (b2* (xn-x0) *(xn-x1))
    return yn