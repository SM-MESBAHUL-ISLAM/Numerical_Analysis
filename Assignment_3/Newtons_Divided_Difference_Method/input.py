import Linear as Li
import Quadratic as Qu
import Cubic as Cu
import Comparison_of_newtonsDivide as ComNewton

def NewtonMethod():
    x_list = list(map(float, input("Enter the values of x: ").strip().split(",")))
    y_list = list(map(float, input("Enter the values of y accourding to the:").strip().split(",")))

    xn = float(input("Enter calculation point xp: "))

    print("Which interpolation method do you want to use?")
    print("1)Linear")
    print("2)Quadratic")
    print("3)Cubic")
    print("4)Compare the performance for different order of polynomial")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        ans = Li.Linear_Interpolation(x_list,y_list,xn)
        print("The ans for %d is: "%xn,ans)
    elif choice == 2:
        ans = Qu.Quadratic_Interpolation(x_list, y_list, xn)
        print("The ans for %d is: " % xn, ans)
    elif choice == 3:
        ans = Cu.Cubic_Interpolation(x_list, y_list, xn)
        print("The ans for %d is: " % xn, ans)
    elif choice == 4:
        ComNewton.Comparison(x_list,y_list,xn)
    else:
        raise Exception('Input Error')

NewtonMethod()