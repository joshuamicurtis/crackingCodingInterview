"""
Rotate Matrix
Given an image represented by an N x N matrix, where each pixel in the image 
is 4 bytes, write a method to rotate the image 90 degrees
"""
def rotate_matrix(matrix):
    if len(matrix) == 0:
        return False
    print "original matrix:"
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
            for row in matrix]))
    for layer in range(len(matrix)/2):
        first = layer
        last = len(matrix) - 1 - layer
        for i in range(first, last):
            offset = i - first
            # save top
            top = matrix[first][i] 
            # left -> top
            matrix[first][i] = matrix[last - offset][first]
            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset] 
            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]
            # top -> right
            matrix[i][last] = top
    print "rotated matrix:"
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
            for row in matrix]))
    return True
N = 5
matrix = [[0 for x in range(N)] for y in range(N)]
matrix[1][0] = 1
matrix[2][0] = 9
'''
for row in matrix:
    for val in row:
        print '{:4}'.format(val),
    print
'''
rotate_matrix(matrix)
print len(matrix)
print len(matrix[0])