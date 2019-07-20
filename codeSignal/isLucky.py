"""
Ticket numbers usually consist of an even number of digits. A ticket number is 
considered lucky if the sum of the first half of the digits is equal to the sum 
of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be isLucky(n) = true;
For n = 239017, the output should be isLucky(n) = false.
"""

def isLucky(n):

    if (len(str(n)) % 2) != 0:
        return False

    s = str(n)
    s1 = s[0:((len(s)//2))]
    sum1 = 0
    for x in s1:
        sum1 += int(x)
    s2 = s[((len(s)//2)):]
    sum2 = 0
    for x in s2:
        sum2 += int(x)

    return sum2 == sum1

print(isLucky(1230))
print(isLucky(239017))
