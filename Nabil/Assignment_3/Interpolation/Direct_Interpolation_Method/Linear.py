import sympy as sy


def Linear_Interpolation(x_values,y_values,xn):
    x = sy.Symbol("x")
    a0 = sy.Symbol("a0")
    a1 = sy.Symbol("a1")

    f = lambda x:a0+a1*x
    eq = lambda a0,a1,x: a0 + a1*x

    for i in range(0,len(x_values)):
        if x_values[i] > xn:
            nearbyPoint = i
            break
    sol = sy.solve((f(x_values[nearbyPoint-1])-y_values[nearbyPoint-1],f(x_values[nearbyPoint])-y_values[nearbyPoint]),(a0,a1))
    result = eq(sol[a0],sol[a1],xn)
    return result

