from extras import valOfFunction, derivativeCalculation, outputFormate


def NewtonRaphsonMethod(coEfficient, numberOfIterations, errorTolerance):
    firstDerivativeCoefficient = derivativeCalculation(coEfficient)

    print("Guess a root: ")
    root = float(input())
    print("\n")

    data = []
    error = 100
    steps = 0

    while (error > errorTolerance and steps < numberOfIterations):
        currentRoot = root - valOfFunction(coEfficient, root)/valOfFunction(
            firstDerivativeCoefficient, root)

        error = abs((currentRoot-root)/root) * 100
        root = currentRoot
        steps += 1
        data.append([steps, round(root, 5), round(error, 5)])

    header = ["Iteration No", "Root", "Error"]

    outputFormate(header, data, root)
