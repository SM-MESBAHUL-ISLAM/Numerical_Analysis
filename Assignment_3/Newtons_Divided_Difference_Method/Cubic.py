import sympy as sy

def Cubic_Interpolation(x_list,y_list,xn):

    xi = sy.Symbol("xi")
    xj = sy.Symbol("xj")
    yi = sy.Symbol("yi")
    yj = sy.Symbol("yj")
    F = lambda xi,xj,yi,yj : (yj-yi)/(xj-xi)

    for i in range(0, len(x_list)):
        if x_list[i] > xn:
            nearbyPoint = i
            break

    x0 = x_list[nearbyPoint-2]
    x1 = x_list[nearbyPoint-1]
    x2 = x_list[nearbyPoint]
    x3 = x_list[nearbyPoint+1]

    y0 = y_list[nearbyPoint-2]
    y1 = y_list[nearbyPoint-1]
    y2 = y_list[nearbyPoint]
    y3 = y_list[nearbyPoint + 1]

    b0 = y0
    b1 = F(x0,x1,y0,y1)
    # print(b1)
    b2 = ( F(x1,x2,y1,y2) - b1 ) / (x2-x0)
    # print(b2)
    p1 = (F(x2,x3,y2,y3) -F(x1,x2,y1,y2)) / (x3-x1)

    p2 = (F(x1,x2,y1,y2) - b1)/ (x2 - x0)
    b3 = (p1 - p2) / (x3 - x0)
    # print(b3)

    yn = b0 + (b1*(xn-x0)) + (b2* (xn-x0) *(xn-x1)) + (b3*(xn-x0)*(xn-x1)*(xn-x2))
    return yn