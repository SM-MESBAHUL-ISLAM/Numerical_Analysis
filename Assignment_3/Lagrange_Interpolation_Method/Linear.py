import  sympy as sy

def Linear_Interpolation(x_list,y_list,xn):

    def test():
        print("Hello there")

    x = sy.Symbol("x")
    xj = sy.Symbol("xj")
    xi = sy.Symbol("xi")


    L = lambda x,xj,xi:(x-xj)/(xi-xj)

    for i in range(0,len(x_list)):
        if x_list[i] > xn:
            nearbyPoint = i
            break
    result = L(xn,x_list[nearbyPoint],x_list[nearbyPoint-1])*y_list[nearbyPoint-1] + L(xn,x_list[nearbyPoint-1],x_list[nearbyPoint])*y_list[nearbyPoint]
    return result
# Linear_Interpolation()