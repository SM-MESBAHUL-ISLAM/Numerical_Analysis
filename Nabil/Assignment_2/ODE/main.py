import Euler as EM
import RungeKutta_Huns as rh
import RungeKutta_Midpoint as rm
import RungeKutta_Ralstons as rr

print("Which ODE method do you want to use to solve the equation dy/dx = 2*y where y = e^(2x)?:")
print("1)Euler Method")
print("2)Runge Kutta Huns Method")
print("3)Runge Kutta Midpoint Method")
print("4)Runge Kutta Ralstons Method")

choice = int(input("Enter your choice: "))

if choice == 1:
    EM.Euler_Method()
elif choice == 2:
    rh.RungeKutta_HunsMethod()
elif choice == 3:
    rm.RungeKutta_MidpointMethod()
elif choice == 4:
    rr.RungeKutta_RalstonsMethod()
else:
    raise Exception('Input Error.')
