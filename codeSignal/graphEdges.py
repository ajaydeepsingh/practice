"""
Count the number of different edges in a given undirected graph with no loops 
and multiple edges.

For: 
matrix = [[false, true, true],
          [true, false, false],
          [true, false, false]]
the output should be graphEdges(matrix) = 2.

"""


def graphEdges(matrix):
    
#     count = 0
#     for i in range(len(matrix)):
#         for j in range(i, len(matrix)):
#             if matrix[i][j]:
#                 count += 1
    
#     return count
#     
    return len([y for x in matrix for y in x if y == True]) / 2

