from backSubstitutionForUpperTriangle import backSubstitutionUpper


def GaussianEliminationMethod(coEfficientMatrix):
    for i in range(len(coEfficientMatrix) - 1):
        for k in range(i+1, len(coEfficientMatrix)):
            multiplication = coEfficientMatrix[k][i]/coEfficientMatrix[i][i]
            for j in range(len(coEfficientMatrix[k])):
                coEfficientMatrix[k][j] = coEfficientMatrix[k][j] - \
                    coEfficientMatrix[i][j]*multiplication

    return backSubstitutionUpper(coEfficientMatrix)
