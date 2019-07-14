"""
Given an integer n and an array a of length n, your task is to apply the following 
mutation to a:

Array a mutates into a new array b of length n.
For each i from 0 to n - 1, b[i] = a[i - 1] + a[i] + a[i + 1].
If some element in the sum a[i - 1] + a[i] + a[i + 1] does not 
exist, it should be set to 0. For example, b[0] should be equal to 0 + a[0] + a[1].
"""



def mutateTheArray(n, a):

    b = [None] * n
    
    if (len(a) == 1):
        b[0] = a[0]
        return b

    for i in range(0, n):
        if i == 0:
            b[i] = 0 + a[i] + a[i + 1]
        elif i == n-1:
            b[i] = a[i-1] + a[i] + 0
        else:
            b[i] = a[i-1] + a[i] + a[i + 1]


    return b