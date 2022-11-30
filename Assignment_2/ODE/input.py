import EulerMethod as EM
import RungeKutta_Huns as RKH
import RungeKutta_Midpoint as RKM
import RungeKutta_Ralstons as RKR

print("Which ODE method do you want to use to solve the equation dy/dx = 2*y where y = e^(2x)?:")
print("1)Euler Method")
print("2)Runge Kutta Huns Method")
print("3)Runge Kutta Midpoint Method")
print("4)Runge Kutta Ralstons Method")

choice = int(input("Enter your choice: "))

if choice == 1:
    EM.Euler_Method()
elif choice == 2:
    RKH.RungeKutta_HunsMethod()
elif choice == 3:
    RKM.RungeKutta_MidpointMethod()
elif choice == 4:
    RKR.RungeKutta_RalstonsMethod()
else:
    raise Exception('Input Error.')
