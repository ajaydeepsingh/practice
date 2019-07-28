"""

The edit distance between two strings refers to the minimum number of character 
insertions, deletions, and substitutions required to change one string to the 
other. For example, the edit distance between 'kitten' and 'sitting' is three: 
substitute the 'k' for 's', substitute the 'e' for 'i', and append a 'g'.

Given two strings, compute the edit distance between them.
"""


def minEditDistance(string1, string2):

    m, n = len(string1), len(string2)

    dp = [[0] * (n+1) for i in xrange(m+1)]

    for i in xrange(n+1):
        dp[0][i] = i

    for j in xrange(m+1):
        dp[j][0] = j

    for i in xrange(1, m+1):
        for j in xrange(1, n+1):
            if string1[i-1] == string2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

    return dp[m][n]


print(minEditDistance("kitten", "sitting"))
print(minEditDistance("hi", "high"))