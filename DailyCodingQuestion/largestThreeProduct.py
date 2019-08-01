"""
Given a list of integers, return the largest product that can be made by
multiplying any three integers.
For example, if the list is [-10, -10, 5, 2], we should return 500,
since that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""


# O(n)
def largestThreeProduct(arr):

    arr.sort()
    return max(arr[0] * arr[1] * arr[-1], arr[-1] * arr[-2] * arr[-3])


print(largestThreeProduct([-1, -2, 0, 3, -5 , 10])) # 100
print(largestThreeProduct([-1, -2, -3, -3, -5 , -4]))



