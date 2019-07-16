"""
Given a string, determine if it is a palindrome, considering only alphanumeric
characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid
palindrome.
"""
import re

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """

    s = s.lower()
    s = s.replace(" ", "")
    s = re.sub('[^A-Za-z0-9]+', '', s)
    # print(s)
    # print(s[::-1])

    return s == s[::-1]


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))