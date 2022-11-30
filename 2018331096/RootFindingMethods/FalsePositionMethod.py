from extras import valOfFunction, outputFormate


def falsePositionMethod(coEfficient, numberOfIterations, errorTolerance):
    print("Please Enter the left and right guess: ")
    left, right = map(float, input().split())
    print("\n")

    
    valueAtLeft = valOfFunction(coEfficient, left)
    valueAtRight = valOfFunction(coEfficient, right)
    if (valueAtRight*valueAtLeft > 0):
        raise Exception('No Solution')

    data = []
    # mid = (high+low)/2
    
    mid = (right*valOfFunction(coEfficient, left) - left*valOfFunction(coEfficient,
           right))/(valOfFunction(coEfficient, left) - valOfFunction(coEfficient, right))
    data.append([1, round(right, 5), round(left, 5), round(mid, 5), "-"])
    indicator = valOfFunction(
        coEfficient, left)*valOfFunction(coEfficient, mid)
    if indicator <= 0:
        right = mid
    else:
        left = mid
    error = 100
    steps = 1
    while (error > errorTolerance and steps < numberOfIterations):
        current_mid = (right*valOfFunction(coEfficient, left) - left*valOfFunction(coEfficient,
                       right))/(valOfFunction(coEfficient, left) - valOfFunction(coEfficient, right))
        indicator = valOfFunction(
            coEfficient, left)*valOfFunction(coEfficient, current_mid)
        if indicator <= 0:
            right = current_mid
        else:
            left = current_mid
        if (valOfFunction(coEfficient, current_mid) == 0):
            error = 0
        else:
            error = abs((current_mid-mid)/mid) * 100
        mid = current_mid
        steps += 1
        data.append([steps, round(right, 5), round(left, 5),
                    round(mid, 5), round(error, 5)])

    header = ["Iteration No.", "Right", "Left", "Mid", "Error"]

    outputFormate(header, data, mid)
