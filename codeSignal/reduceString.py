"""
You are given a string. Remove its first and last characters until the string is
empty or the first and the last characters are not equal. Output the resulting
string.
"""

def reduceString(inputString):
    
    if inputString == "":
            return ""
    if inputString[0] == inputString[-1]:
        return reduceString(inputString[1:-1])
    else:
        return inputString

