"""
Write a program which takes an array of n integersm where A[i] denotes the maximum you can advance from index i ,
and returns whether it is possible to advance to the last index starting from the begging of the array.
"""

# helper, greedy approach from the end, might not work
def CanReachEnd(A, target) -> bool:
    gap = 1
    # target == index, target - gap == distance/separation
    while target > 0 and target - gap > -1:
        if A[target - gap] >= gap:
            target = target - gap
            gap = 1
        else:
            gap += 1

    return target == 0


#       O(n)
def can_reach_end(A):
    return CanReachEnd(A, len(A) - 1)


# solution 2 (keeping sum of where we can reach)
def simlpleCanReachEnd(A):
    index = 0
    furthestReach, target = 0, len(A) - 1
    while index <= furthestReach and furthestReach < target:
        furthestReach = max(furthestReach, A[index] + index)
    return furthestReach >= target


if __name__ == "__main__":
    print(can_reach_end([2, 4, 1, 1, 0, 2, 3]))
