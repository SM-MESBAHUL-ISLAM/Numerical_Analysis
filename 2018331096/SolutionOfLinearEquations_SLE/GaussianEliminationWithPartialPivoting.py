from backSubstitutionForUpperTriangle import backSubstitutionUpper


def GaussianEliminationWithPartialPivotingMethod(coEfficientMatrix):
    for i in range(len(coEfficientMatrix) - 1):
        maxRow = i
        maxValue = coEfficientMatrix[i][i]
        
        for j in range(i+1, len(coEfficientMatrix)):
            if abs(coEfficientMatrix[j][i]) > maxValue:
                maxValue = abs(coEfficientMatrix[j][i])
                maxRow = j

        coEfficientMatrix[i], coEfficientMatrix[maxRow] = coEfficientMatrix[maxRow], coEfficientMatrix[i]

        for k in range(i+1, len(coEfficientMatrix)):
            multiplication = coEfficientMatrix[k][i]/coEfficientMatrix[i][i]
            for j in range(len(coEfficientMatrix[k])):
                coEfficientMatrix[k][j] = coEfficientMatrix[k][j] - \
                    coEfficientMatrix[i][j]*multiplication

    return backSubstitutionUpper(coEfficientMatrix)
