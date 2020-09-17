# * Question:
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# Find all the elements of [1, n] inclusive that do not appear in this array.
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
# * Example:
# * Input:
# [4,3,2,7,8,2,3,1]
# * Output:
# [5,6]


# Solution

# helper function

def CyclicConversion(arr, startingIndex):
    while arr[startingIndex] != -1:
        temp = arr[startingIndex]
        arr[startingIndex] = -1
        startingIndex = temp - 1


def numsDisappeared(nums):
    output = []
    for num in nums:
        if num != -1:
            CyclicConversion(nums, num-1)
    for i in range(len(nums)):
        if nums[i] != -1:
            output.append(i+1)

    return output


def magnitudeShift(nums):
    output = []
    for num in nums:
        num = abs(num)
        if nums[num-1] > 0:
            nums[num-1] *= -1

    for i in range(len(nums)):
        if nums[i] > 0:
            output.append(i+1)

    return output


if __name__ == "__main__":
    input1 = [4, 3, 2, 7, 8, 2, 3, 1]
    input2 = [1, 1, 1, 1, 1]
    print(numsDisappeared(input2))
