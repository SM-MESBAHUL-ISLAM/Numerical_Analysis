from BisectionMethod import bisectionMethod
from FalsePositionMethod import falsePositionMethod
from NewtonRaphsonMethod import NewtonRaphsonMethod
from SecantMethod import SecantMethod
from extras import formateInput

coEfficient, numberOfIterations, errorTolerance = formateInput()

print("Which root finding method do you want to use?: ")
print("1. Bisection Method \n2. False Position Method\n3. Newton Raphson Method\n4. Secant Method")

choice = int(input())

if choice == 1:
    bisectionMethod(coEfficient, numberOfIterations, errorTolerance)
elif choice == 2:
    falsePositionMethod(coEfficient, numberOfIterations, errorTolerance)
elif choice == 3:
    NewtonRaphsonMethod(coEfficient, numberOfIterations, errorTolerance)
elif choice == 4:
    SecantMethod(coEfficient, numberOfIterations, errorTolerance)
else:
    raise Exception('Input Error')
