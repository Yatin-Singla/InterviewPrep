'''
Write a program which takes as input a sorted array and updates it so that all duplicates have been removed
and the remaining elements have been shifted left to fill the emptied indices.
Return the number of valid elements. Cannot use library functions
'''


# def DelDup(A):
#     if not A:
#         return 0
#     # the element in the first index (0) will be unique. so start from index 1.
#     writeIndex = 1
#     for index in range(1, len(A)):
#         # index -1 will have the first occurence of the repeat character.
#         A[writeIndex - 1] != A[index]:
#             A[writeIndex] = A[index]
#             writeIndex += 1
#     return writeIndex


def removeDuplicates(A):
    freeSpot = 1
    for i in range(1, len(A)):
        if A[i] != A[i-1]:
            A[freeSpot] = A[i]
            freeSpot += 1
    return A[:freeSpot]


if __name__ == "__main__":
    # print(DepDup([2,3,5,5,7,11,11,11,13]))
    print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
