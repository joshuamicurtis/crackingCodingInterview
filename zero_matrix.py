"""
Write an algorithm such that if an element of an MxN matrix is 0, its 
entire row and column are set to ).
"""
def zero_matrix(matrix):
    topZero = False
    print "original matrix:"
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
            for row in matrix]))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[0][j] = '   C'
                matrix[i][0] = '   R'
                if i == 0:
                    topZero = True
    print "zeros added to edge of matrix:"
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
            for row in matrix])) 
    for i in range(len(matrix)):
        if matrix[i][0] == '   R':
            for j in range(len(matrix[i])):
                if matrix[i][j] != '   C':
                    matrix[i][j] = 0
    print "change rows matrix:"
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
            for row in matrix])) 
    for j in range(len(matrix[0])):
        if matrix[0][j] == '   C':
            for i in range(len(matrix)):
                matrix[i][j] = 0
    if topZero == True:
        for z in range(len(matrix)-1):
            matrix[0][z] = 0
    print "final matrix:"
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
            for row in matrix]))        

matrix = [[1 for x in range(5)] for y in range(6)]
matrix[0][3] = 0
matrix[2][0] = 0

zero_matrix(matrix)            