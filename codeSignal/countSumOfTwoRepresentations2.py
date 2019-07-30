"""
Given integers n, l and r, find the number of ways to represent n as a sum of 
two integers A and B such that l ≤ A ≤ B ≤ r.
"""

def countSumOfTwoRepresentations2(n, l, r):
    s = 0
    for i in range(l, r + 1):
        if i <= n - i <= r:
            s += 1
    return s