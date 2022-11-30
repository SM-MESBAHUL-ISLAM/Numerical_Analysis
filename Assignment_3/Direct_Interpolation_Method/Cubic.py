import sympy as sy
def Cubic_Interpolation(x_list,y_list,xn):
    x = sy.Symbol("x")
    a0 = sy.Symbol("a0")
    a1 = sy.Symbol("a1")
    a2 = sy.Symbol("a2")
    a3 = sy.Symbol("a3")

    f = lambda x:(a0+a1*x+a2*(x**2)+a3*(x**3))
    eq = lambda a0,a1,a2,a3,x:(a0+a1*x+a2*(x**2)+a3*(x**3))

    for i in range(0,len(x_list)):
        if x_list[i] > xn:
            nearbyPoint = i
            break

    sol = sy.solve((f(x_list[nearbyPoint-2]) - y_list[nearbyPoint-2],f(x_list[nearbyPoint-1]) - y_list[nearbyPoint-1],f(x_list[nearbyPoint])-y_list[nearbyPoint],f(x_list[nearbyPoint+1])-y_list[nearbyPoint+1]),(a0,a1,a2,a3))
    result = eq(sol[a0],sol[a1],sol[a2],sol[a3],xn)
    return result

# Quadratic_Interpolation()