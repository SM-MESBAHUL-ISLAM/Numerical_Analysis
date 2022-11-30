def backSubstitutionLower(lowerMatrix):
    ans = [0]*(len(lowerMatrix))
    for i in range(len(lowerMatrix)):
        sum = 0
        for j in range(i):
            sum += lowerMatrix[i][j]*ans[j]
        ans[i] = (lowerMatrix[i][len(
            lowerMatrix)] - sum)/lowerMatrix[i][i]
    return ans
