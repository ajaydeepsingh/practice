"""
Given two strings, find the number of common characters between them.

For s1 = "aabcc" and s2 = "adcaa"
the output should be commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".

"""

def commonCharacterCount(s1, s2):

    chars = set()
    for char in s1:
        chars.add(char)

    count = 0
    
    chars2 = set()
    for char in s2:
        chars2.add(char)

    return(len(chars.intersection(chars2)))



# def commonCharacterCount(s1, s2):
#     com = [min(s1.count(i), s2.count(i)) for i in set(s1)]
#     return sum(com)

