from extras import valOfFunction, outputFormate


def SecantMethod(coEfficient, numberOfIterations, errorTolerance):

    print("Please enter two guesses of the root: ")
    prevRoot, currRoot = map(float, input().split())
    print("\n")

    data = []
    error = 100
    steps = 0

    while (error > errorTolerance and steps < numberOfIterations):
        currentRoot = currRoot - (valOfFunction(coEfficient, currRoot)*(currRoot-prevRoot))/(
            valOfFunction(coEfficient, currRoot) - valOfFunction(coEfficient, prevRoot))

        error = abs((currentRoot-currRoot)/currRoot) * 100
        prevRoot = currRoot
        currRoot = currentRoot
        steps += 1
        data.append([steps, round(prevRoot, 5),
                    round(currRoot, 5), round(error, 5)])

    header = ["Iteration No.", "root previous", "root", "error"]

    outputFormate(header, data, currRoot)
