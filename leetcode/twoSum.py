"""
Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.
"""


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    s = {}
    for i, n in enumerate(nums):
        m = target - n

        if m in s:
            return [s[m], i]
        else:
            s[n] = i


print(twoSum([2, 7, 11, 15], 9))
