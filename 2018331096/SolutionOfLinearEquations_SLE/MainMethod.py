from GaussianElimination import GaussianEliminationMethod
from GaussianEliminationWithPartialPivoting import GaussianEliminationWithPartialPivotingMethod
from LU_decomposition import inverseMatrix
from Formation import formationInput
from select import select




print("Choose your objective:\n1. Solve the System of Linear Equation\n2. Inverse Matrix")

def printResult(result):
    print("The solution of the system is:")
    for i in range(len(result)):
        print('X' + str(i+1) + " = " + str(result[i]))

choice = int(input())
print("\n")

if choice == 1:
    print("Please Enter your choice:")
    print("1. Naive Gaussian Elimination Method")
    print("2. Gaussian Elimination with Partial Pivoting Method")
    anotherChoice = int(input())
    print("\n")

    if (anotherChoice == 1):
        CoefficientMatrix = formationInput()
        printResult(GaussianEliminationMethod(CoefficientMatrix))
    elif anotherChoice == 2:
        CoefficientMatrix = formationInput()
        printResult(
            GaussianEliminationWithPartialPivotingMethod(CoefficientMatrix))
    else:
        raise Exception('Error!!')
elif choice == 2:
    inverseMatrix()
else:
    raise Exception("Error!!!")
