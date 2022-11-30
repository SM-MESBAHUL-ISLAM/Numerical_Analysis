import  sympy as sy

def Linear_Interpolation(x_values,y_values,xf):


    x = sy.Symbol("x")
    xj = sy.Symbol("xj")
    xi = sy.Symbol("xi")


    L = lambda x,xj,xi:(x-xj)/(xi-xj)

    for i in range(0,len(x_values)):
        if x_values[i] > xf:
            closePoint = i
            break
    result = L(xf,x_values[closePoint],x_values[closePoint-1])*y_values[closePoint-1] + L(xf,x_values[closePoint-1],x_values[closePoint])*y_values[closePoint]
    return result
