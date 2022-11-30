import sympy as sy
import numpy as np
from sympy import symbols, Eq, solve


def QuadraticInterpolation():
    num = int(input("Number of elements in the array:- "))
    x_list = list(map(float, input("elements of array:-").strip().split(",")))
    # print(x_list)

    y_list = list(map(float, input("elements of array:-").strip().split(",")))
    # print(y_list)

    xn = float(input("Enter calculation point xp: "))
    for i in range(0, num):
        if x_list[i] > xn:
            pos = i
            break

    pos = pos -1
    need = pos + 2
    if need>=num :
        pos = pos-1

    need = pos + 2
    if need >= num:
        pos = pos - 1

    x, y, z = symbols('x y z')
    eq1 = Eq(x + (y * x_list[pos]) + (z * x_list[pos] * x_list[pos]) - y_list[pos])
    eq2 = Eq(x + (y * x_list[pos + 1]) + (z * x_list[pos + 1] * x_list[pos + 1]) -y_list[pos+1])
    eq3 = Eq(x + (y * x_list[pos + 2]) + (z * x_list[pos + 2] * x_list[pos + 2]) - y_list[pos+2])

    sol_dict = solve((eq1, eq2, eq3), (x, y, z))
    #print(f'x = {sol_dict[x]}')
    #print(f'y = {sol_dict[y]}')
    #print(f'z = {sol_dict[z]}')

    answer = sol_dict[x] + (sol_dict[y]*xn) + (sol_dict[z]*xn*xn)
    print("Interpolatiog point : ")
    print('%.4f' %answer)

QuadraticInterpolation()