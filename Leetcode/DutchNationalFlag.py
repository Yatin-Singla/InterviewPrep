"""
Given an array A and an index i in to A, rearrrange the elements such that all elements less than A[i] appear first,
 followed by the elements equal to the pivot followed by elements greater than the pivot.
"""

# solution 1
#   time complexity         space complexity
#       O(n)                      O(n)
def DutchNationalFlag(A, i):
    left, equal, right = [], [], []
    for item in A:
        if item < A[i]:
            left.append(item)
        elif item == A[i]:
            equal.append(item)
        else:
            right.append(item)
    equal.extend(right)
    left.extend(equal)
    return left


# solution 2 (Most sophisticated)
#       O(n)                        O(1)
def DutchNationalFlagEfficient(A: list, pivotIndex: int):
    # bottom = A[:smaller]
    # middle = A[smaller:equal]
    # unclassified = A[equal:larger]
    # top = A[larger:]
    smaller, equal, larger = 0, 0, len(A)

    while equal < larger:
        if A[equal] < A[pivotIndex]:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == A[pivotIndex]:
            equal += 1
        else:  # A[equal] > A[pivotIndex]:
            larger -= 1
            A[larger], A[equal] = A[equal], A[larger]
    return A


# solution 3 less sophisticated
#   O(n)                O(1)
# reserve the seat for digits less than pivot in the front
# now reserve the seat for the digits greater that the pivot in the back.
def DutchNationalFlagLessSophisticated(A: list, pivotIndex: int):
    smaller = 0
    for index in range(len(A)):
        if A[index] < A[pivotIndex]:
            A[smaller], A[index] = A[index], A[smaller]
            smaller += 1
    larger = len(A) - 1
    # ? Small optimization might be iterating range(len(A)-1, smaller, -1)
    for index in reversed(range(len(A))):
        if A[index] > A[pivotIndex]:
            A[larger], A[index] = A[index], A[larger]
            larger -= 1
    return A


if __name__ == "__main__":
    arr = [-7, 10, 2, 5, 4, 8, 7, 3, 0, 9]
    index = 4
    print(DutchNationalFlagLessSophisticated(arr, index))
    print(arr[index])
