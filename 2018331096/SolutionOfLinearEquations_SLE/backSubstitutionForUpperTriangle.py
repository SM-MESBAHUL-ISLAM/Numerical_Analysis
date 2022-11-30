def backSubstitutionUpper(coEfficientMatrix):
    ans = [0]*(len(coEfficientMatrix))
    for i in range(len(coEfficientMatrix)-1, -1, -1):
        sum = 0
        for j in range(len(coEfficientMatrix)-1, i, -1):
            sum += coEfficientMatrix[i][j]*ans[j]
        ans[i] = (coEfficientMatrix[i][len(
            coEfficientMatrix)] - sum)/coEfficientMatrix[i][i]
    return ans
