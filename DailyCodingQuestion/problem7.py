# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the
# number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be decoded
# as 'aaa', 'ka', and 'ak'.
#
# You can assume that the messages are decodable.
# For example, '001' is not allowed.


## Hint Dynamic programming


def decodeCount(message):
    messageLength = len(message)
    count = [0] * (messageLength+1)
    count[0] = 1
    count[1] = 1

    for i in range (2, messageLength + 1):
        count[i] = 0
        if message[i-1] > '0':
            count[i] = count[i-1]

        if (message[i-2] == '1' or (message[i-2] == '2' and message[i-1] < '7') ):
            count[i] += count[i-2]


    return count[messageLength]



# driver code

print(decodeCount('1234'))
print(decodeCount('2342'))
print(decodeCount('0'))
print(decodeCount('1000'))
