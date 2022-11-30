

def Linear_Interpolation(x_list,y_list,xn):

    for i in range(0, len(x_list)):
        if x_list[i] > xn:
            nearbyPoint = i
            break

    x0 = x_list[nearbyPoint-1]
    x1 = x_list[nearbyPoint]
    y0 = y_list[nearbyPoint-1]
    y1 = y_list[nearbyPoint]

    b0 = y0
    b1 = (y1 - y0)/ (x1 - x0)

    yn = b0 + b1*(xn - x0)
    return yn
