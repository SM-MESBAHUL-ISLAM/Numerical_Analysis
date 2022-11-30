from GaussianElimination import GaussianEliminationMethod
from GaussianEliminationWithPartialPivoting import GaussianEliminationWithPartialPivotingMethod
from LUMatrixCalculation import findLU


def formationInput():
    print("Number of unknowns?:")
    numberOfUnknown = int(input())
    print("\n")

    coEfficientMatrix = []
    for i in range(numberOfUnknown):
        print("Please Enter the coefficients of the " + str(i+1) + "th equation: ")

        for i in range(numberOfUnknown+1):
            if i == numberOfUnknown:
                print(chr(i+97), end='\n')
            elif i == numberOfUnknown - 1:
                print(f'{chr(i+97)}x{i + 1}', end=' = ')
            else:
                print(f'{chr(i+97)}x{i + 1}', end=' + ')

        coEfficient = list(map(float, input().split()))

        if len(coEfficient) != numberOfUnknown + 1:
            raise Exception('ERROR!Number of Coefficient must be equal to (number of unknown + 1)!!')

        coEfficientMatrix.append(coEfficient)
    return coEfficientMatrix
