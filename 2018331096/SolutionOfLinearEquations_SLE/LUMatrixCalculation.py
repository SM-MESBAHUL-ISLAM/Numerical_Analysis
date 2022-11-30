from copy import deepcopy


def findLU(upperTriangularMatrix):
    n = len(upperTriangularMatrix)
    lowerTriangularMatrix = deepcopy(upperTriangularMatrix)

    for i in range(len(lowerTriangularMatrix)):
        for j in range(len(lowerTriangularMatrix[i])):
            if i == j:
                lowerTriangularMatrix[i][j] = 1
            elif j > i:
                lowerTriangularMatrix[i][j] = 0

    for i in range(len(upperTriangularMatrix) - 1):
        for k in range(i+1, len(upperTriangularMatrix)):
            multiplier = upperTriangularMatrix[k][i] / \
                upperTriangularMatrix[i][i]
            lowerTriangularMatrix[k][i] = multiplier
            for j in range(len(upperTriangularMatrix[k])):
                upperTriangularMatrix[k][j] = upperTriangularMatrix[k][j] - \
                    upperTriangularMatrix[i][j]*multiplier
    return upperTriangularMatrix, lowerTriangularMatrix
