'''
Given an image represented by NxN matrix, where each pixel in the image is 4 bytes, 
write a method to rotate the image by 90degrees. Can you do this in place?
'''

#helper function which prints matrix
def PrintMatrix(mat):
    for row in mat:
        print(row)

def RotateMatrix(mat):
    PrintMatrix(mat)
    print("-----------After-----------")
    copyMatrix = [[i for i in row] for row in mat]
    N = len(mat)
    for row in range(N):
        for col in range(N):
            mat[row][col] = copyMatrix[N-1-col][row]

    return mat

#          O(n)             O(1)

def swap(mat, start, stop):
    temp = mat[start][start]

def RotateMatrixEfficient(mat):
    N = len(mat)
    start = 0
    stop = N - 1
    while start < stop:
        for iteration in range(start, stop):
            swap(mat, start, stop)
        start += 1
        stop -= 1  
if __name__ == "__main__":
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    PrintMatrix(RotateMatrix(mat))