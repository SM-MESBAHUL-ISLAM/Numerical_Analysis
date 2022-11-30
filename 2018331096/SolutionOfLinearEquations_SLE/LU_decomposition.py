from LUMatrixCalculation import findLU
from backSubstitutionForLowerTriangle import backSubstitutionLower
from backSubstitutionForUpperTriangle import backSubstitutionUpper


def inverseMatrix():
    print("Enter the Order of the square matrix:",end="")
    orderOfMatrix = int(input())
    print("")
    if orderOfMatrix < 1:
        raise Exception("Order must be a positive integer greater or equal to 1!!!")

    matrix = []

    for i in range(orderOfMatrix):
        print("please enter the " + str(i+1) + "th row of the matrix(ie: value1 value2): ",end="")
        temp = list(map(float, input().split()))
        if len(temp) != orderOfMatrix:
            raise Exception("Error!Not enough value is given!!!")
        matrix.append(temp)
    Upper, Lower = findLU(matrix)

    for row in Lower:
        row.append(0)

    for j in range(orderOfMatrix):
        Upper[j].append(0)
    inverseMatrix = []

    for i in range(orderOfMatrix):
        Lower[i][len(Lower)] = 1

        tran = backSubstitutionLower(Lower)

        for j in range(orderOfMatrix):
            Upper[j][len(Upper)] = tran[j]
        result = backSubstitutionUpper(Upper)

        inverseMatrix.append(result)
        Lower[i][len(Lower)] = 0

    for i in range(orderOfMatrix):
        for j in range(i+1):
            inverseMatrix[i][j], inverseMatrix[j][i] = round(
                inverseMatrix[j][i], 5), round(inverseMatrix[i][j], 5)

    print("The inverse of the given matrix is:")
    print()

    format_row = "{:>12}" * (len(inverseMatrix[0]))
    for row in inverseMatrix:
        print(format_row.format(*row))
