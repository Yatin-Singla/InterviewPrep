'''
Write a program that takes an array A of n numbers,
and rearranges A's elements to get a new array B having the property that 
B[0] <= B[1] >= B[2] <= B[3] >= B[4] <= B[5] >= ......
'''

def ComputeAlternation(A: [int]):
    A.sort()
    print(A)
    for Fptr in range(0, len(A)-1, 2):
        temp = A[Fptr]
        A[Fptr] = A[Fptr + 1]
        A[Fptr + 1] = temp

    return A

if __name__ == "__main__":
    print(ComputeAlternation([12,11,13,9,12,8,14,13,15]))
