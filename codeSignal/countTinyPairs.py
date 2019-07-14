"""
You are given two arrays of integers a and b of the same length, and an integer k. 
We will be iterating through array a from left to right, and simultaneously through array b 
from right to left, and looking at pairs (x, y), where x is from a and y is from b. 
Such a pair is called tiny if the concatenation xy is strictly less than k.

Your task is to return the number of tiny pairs that you'll encounter during 
the simultaneous iteration through a and b.

"""

def countTinyPairs(a, b, k):

    count = 0
    for i in range(0,len(a)):

        temp1 = a[i]
        temp2 = b[len(a)- 1 - i]

        part1 = str(temp1)
        part2 = str(temp2)

        tog = part1 + part2

        if (int(tog) < k):
            count += 1

    return count






