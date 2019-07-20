"""
Given an array of strings, return another array containing all of its longest
strings.
"""


def allLongestStrings(inputArray):

    longest = len(inputArray[0])
    newArray = []

    for x in inputArray:
        if len(x) > longest:
            longest = len(x)
            newArray = []
            newArray.append(x)
        elif len(x) == longest:
            newArray.append(x)

    return newArray

