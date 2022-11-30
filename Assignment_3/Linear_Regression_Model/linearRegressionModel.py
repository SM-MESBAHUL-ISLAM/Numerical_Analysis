import numpy as np
from matplotlib import pyplot as plt

def lin_regression_model():
    x_list = list(map(float,input("Enter the values of x coordinate: ").strip().split(",")))
    y_list = list(map(float,input("Enter the values of y coordinate").strip().split(",")))

    x = np.array(x_list)
    y = np.array(y_list)

    x_mean = np.mean(x)
    y_mean = np.mean(y)

    n = len(x_list)
    x1 = ((n*np.sum(y*x) - (np.sum(x) * np.sum(y))))/((n * np.sum(x*x) - (np.sum(x) * np.sum(x))))
    y1 = y_mean - x1*x_mean

    print("Solving for x1 and y1 yields: ")
    print("x1 = ",x1,"and y1 = ",y1)

    plt.scatter(x,y,color='g',marker="o")
    y_curve = y1 + x1*x

    plt.plot(x,y_curve,'b')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

lin_regression_model()