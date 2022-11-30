

def Linear_Interpolation(x_values,y_values,xf):

    for i in range(0, len(x_values)):
        if x_values[i] > xf:
            closePoint = i
            break

    x0 = x_values[closePoint-1]
    x1 = x_values[closePoint]
    y0 = y_values[closePoint-1]
    y1 = y_values[closePoint]

    b0 = y0
    b1 = (y1 - y0)/ (x1 - x0)

    ans = b0 + b1*(xf - x0)
    return ans
