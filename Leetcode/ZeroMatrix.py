'''
WRITE AN ALGORITHM SUCH THAT IF AN ELEMENT IS AN MXN MATRIX IS 0,
ITS ENTIRE ROW AND COLUMN ARE SET TO 0.
'''

#helper function which prints matrix
def PrintMatrix(mat):
    for row in mat:
        print(row)

def ZeroMatrix(mat):
    result = []
    PrintMatrix(mat)
    print("---------After--------")
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            if mat[row][col] == 0:
                result.append((row,col))
    for row,col in result:
        #set row 0
        for ZeroCol in range(len(mat[0])):
            mat[row][ZeroCol] = 0
        for ZeroRow in range(len(mat)):
            mat[ZeroRow][col] = 0

    return mat


#       O(n)            O(1)
'''
Step 1: check row 0 and col 0 for any zeroes, if so set rowHasZero and colHasZero appropriately.
Step 2: iterate over the matrix and set row mat[i][0] = 0 and mat[0][j] = 0 if mat[i][j] = 0
Step 3: nullify the entire row for which mat[i][0] = 0
Step 4: nullify the entire col for which mat[0][j] = 0
Step 5: nullify entire row and col accordingly based upon rowHasZero, colHasZero
'''

def nullifyRow(mat, row):
    for col in range(len(mat[0])):
        mat[row][col] = 0
def nullifyCol(mat, col):
    for row in range(len(mat)):
        mat[row][col] = 0
def ZeroMatrixEfficient(mat):
    if not mat:
        return mat
    
    rowHasZero = False
    colHasZero = False
    #Step 1:
    for col in range(len(mat[0])):
        if mat[0][col] == 0:
            rowHasZero = True
            break
    for row in range(len(mat)):
        if mat[row][0] == 0:
            colHasZero = True
            break
    #Step 2:
    #assuming MxN, N > 1
    for row in range(1, len(mat)):
        for col in range(1, len(mat[0])):
            if mat[row][col] == 0:
                mat[0][col] = 0
                mat[row][0] = 0

    #Step 3:
    for row in range(len(mat)):
        if mat[row][0] == 0:
            nullifyRow(mat, row)
    #Step 4:
    for col in range(len(mat[0])):
        if mat[0][col] == 0:
            nullifyCol(mat, col)
    
    #Step 5:
    if rowHasZero:
        nullifyRow(mat, 0)
    if colHasZero:
        nullifyCol(mat, 0)

    return mat
    
if __name__ == "__main__":
    mat = [[1,2,3],[4,0,5],[6,7,8]]
    PrintMatrix(ZeroMatrixEfficient(mat))
