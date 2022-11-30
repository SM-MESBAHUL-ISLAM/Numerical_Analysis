def outputFormate(heading, valu, ans):
    format_row = "{:>15}" * (len(heading))
    print(format_row.format(*heading))
    for row in valu:
        print(format_row.format(*row))
    print("Root of the equation = " + str(ans))

def derivativeCalculation(coEfficient):
    newCoefficients = []
    for i in range(len(coEfficient) - 1):
        newCoefficients.append(coEfficient[i]*(len(coEfficient)-i-1))
    return newCoefficients

def valOfFunction(coEfficient, x):
    val = 0
    for i in range(len(coEfficient)):
        val += coEfficient[i]*(x**(len(coEfficient)-i-1))
    return val

def formateInput():
    print("Please enter the order of polynomial equation: ")
    polynomialOrder = int(input())
    print("\n")
    if polynomialOrder < 1:
        raise Exception('Error!Order must be greater or equal to 1!!!')

    print("Please Enter the coefficients separeted by space:")

    for i in range(polynomialOrder+1):
        if i == polynomialOrder:
            print(chr(i+97), end=' = 0\n')
        elif i == polynomialOrder - 1:
            print(f'{chr(i+97)}x', end=' + ')
        else:
            print(f'{chr(i+97)}x^{polynomialOrder-i}', end=' + ')

    coEfficient = list(map(float, input().split()))
    print("\n")

    if len(coEfficient) != polynomialOrder + 1:
        raise Exception('Error! Number of Coefficients is must be equal to (order+1)!!!')

    print("Please select the method: ")
    print("1. By Number of Iterations")
    print("2. By Error Tolerance")
    print("3. By Number of Significant Digits")

    case = int(input())
    print("\n")

    numberOfIterations = 10000000
    errorTolerance = 0

    if case == 1:
        print("Please enter the number of Iterations: ")
        numberOfIterations = int(input())
        print("\n")
    elif case == 2:
        print("Give the amount of error tolerance(in percentage):")
        errorTolerance = float(input())
        print("\n")
    elif case == 3:
        print("Please enter the number of significant digits:")
        no_of_significant_digits = int(input())
        print("\n")
        errorTolerance = .5*10**(2-no_of_significant_digits)
    else:
        raise Exception('Input error!!')

    return coEfficient, numberOfIterations, errorTolerance
