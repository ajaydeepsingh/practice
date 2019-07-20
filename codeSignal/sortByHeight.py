"""
Some people are standing in a row in a park. There are trees between them which
cannot be moved. Your task is to rearrange the people by their heights in a
non-descending order without moving the trees. People can be very tall!

a = [-1, 150, 190, 170, -1, -1, 160, 180] -> [-1, 150, 160, 170, -1, -1, 180, 190].


"""

def sortByHeight(a):
    l1 = sorted([x for x in a if x != -1])
    for i, j in enumerate(a):
        if j == -1:
            l1.insert(i, j)
    return(l1)