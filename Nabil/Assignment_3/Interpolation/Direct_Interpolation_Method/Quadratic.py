import sympy as sy


def Quadratic_Interpolation(x_values,y_values,xf):
    x = sy.Symbol("x")
    a0 = sy.Symbol("a0")
    a1 = sy.Symbol("a1")
    a2 = sy.Symbol("a2")

    f = lambda x:(a0+a1*x+a2*(x**2))
    equation = lambda a0,a1,a2,x:(a0+a1*x+a2*(x**2))

    for i in range(0,len(x_values)):
        if x_values[i] > xf:
            nearbyPoint = i
            break

    sol = sy.solve((f(x_values[nearbyPoint-2]) - y_values[nearbyPoint-2],f(x_values[nearbyPoint-1]) - y_values[nearbyPoint-1],f(x_values[nearbyPoint])-y_values[nearbyPoint]),(a0,a1,a2))
    result = equation(sol[a0],sol[a1],sol[a2],xf)
    return result
