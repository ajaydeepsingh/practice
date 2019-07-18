def arrayMaximalAdjacentDifference(inputArray):
    diff = 0
    for i in range(0, len(inputArray) - 1):
        if abs(inputArray[i] - inputArray[i+1]) > abs(diff):
            diff = abs(inputArray[i] - inputArray[i+1])

    return diff