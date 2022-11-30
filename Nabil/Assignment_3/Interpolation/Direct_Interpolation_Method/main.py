import Linear as Li
import Quadratic as Qu
import Cubic as Cu
import Comparison as ComDirect

def DirectInterpolation():
    x_values = list(map(float, input("Enter the values of x: ").strip().split(",")))
    y_values = list(map(float, input("Enter the values of y accourding to the:").strip().split(",")))

    xf = float(input("Enter calculation point xp: "))

    print("Which interpolation method do you want to use?")
    print("1)Linear")
    print("2)Quadratic")
    print("3)Cubic")
    print("4)Compare the performance for different order of polynomial")

    option = int(input("Enter your option: "))
    if option == 1:
        ans = Li.Linear_Interpolation(x_values,y_values,xf)
        print("The ans for %d is: "%xf,ans)
    elif option == 2:
        ans = Qu.Quadratic_Interpolation(x_values, y_values, xf)
        print("The ans for %d is: " % xf, ans)
    elif option == 3:
        ans = Cu.Cubic_Interpolation(x_values, y_values, xf)
        print("The ans for %d is: " % xf, ans)
    elif option == 4:
        ComDirect.Comparison(x_values,y_values,xf)
    else:
        raise Exception('Input Error')
DirectInterpolation()