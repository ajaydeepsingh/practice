"""
You are given an n x n 2D matrix that represents an image.
Rotate the image by 90 degrees (clockwise).
"""


def rotateImage(a):
    n = len(a)

    # first transpose
    for i in range(n):
        for j in range(i + 1, n):
            temp = a[i][j]
            a[i][j] = a[j][i]
            a[j][i] = temp

    # flip horizontally
    for i in range(n):
        for j in range(n // 2):
            temp = a[i][j]
            a[i][j] = a[i][n - 1 - j]
            a[i][n - 1 - j] = temp

    return a
