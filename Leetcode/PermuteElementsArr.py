'''
Given an array A of n elements and a permutation P, apply P to A
Permutation is specified by an array P, where P[i] represents the location of the element at i in the permutatuion.
eg P = <2,0,1,3> and A = <a,b,c,d>, solution = <b,c,a,d>
'''

def applyPermutation(A: [any], P: [int])-> [any]:
    length = len(P)
    result = [None]*length
    for index in range(length):
        result[P[index]] = A[index]

    return result

def PermutationPlace(A, P):
    index = swap = 0
    temp = A[index]
    while swap < len(A):
        A[index] = temp
        temp = A[P[index]]
        A[P[index]] = A[index]
        index = P[P[index]]
        swap += 1
    

if __name__ == "__main__":
    print(applyPermutation(['a','b','c','d'], [2,0,1,3]))
