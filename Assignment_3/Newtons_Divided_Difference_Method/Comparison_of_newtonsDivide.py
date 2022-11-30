import Cubic as Cu
import Linear as Li
import Quadratic as Qu
def Comparison(x_list,y_list,xn):
    ans_of_linear = Li.Linear_Interpolation(x_list,y_list,xn)
    ans_of_quadratic = Qu.Quadratic_Interpolation(x_list,y_list,xn)
    ans_of_cubic = Cu.Cubic_Interpolation(x_list,y_list,xn)

    #comparison table
    print("Order of Polynomial\t\t\t\t    :Linear \t\t Quadratic \t\t Cubic")
    e2=(abs(ans_of_linear - ans_of_quadratic)/ans_of_linear)*100
    e3 = (abs(ans_of_quadratic - ans_of_cubic)/ans_of_quadratic)*100

    print("y(%f)\t\t\t\t\t   : %f \t %f \t %f"%(xn,ans_of_linear,ans_of_quadratic,ans_of_cubic))
    print("Absolute Relative Approximate Error: -----\t\t %.5f \t\t %.5f"%(e2,e3))
