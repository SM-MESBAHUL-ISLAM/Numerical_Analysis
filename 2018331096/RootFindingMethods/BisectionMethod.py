from extras import valOfFunction, outputFormate


def bisectionMethod(coEfficient, numberOfIterations, errorTolerance):
    print("Please Enter two guesses: ")
    left, right = map(float, input().split())
    print("\n\n")

    valueAtLeft = valOfFunction(coEfficient, left)
    valueAtRight = valOfFunction(coEfficient, right)
    if (valueAtRight*valueAtLeft > 0):
        raise Exception('No Solution Exist')
    data = []
    mid = (right+left)/2
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
        current_mid = (right+left)/2
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
