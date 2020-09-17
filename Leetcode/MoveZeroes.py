# Question: Given an array nums, write a function to move all 0's
# to the end of it while maintaining the relative order of the non-zero elements.

def moveZeroes(nums):
    insertIndex = 0
    lenN = len(nums)
    for rollingIndex in range(lenN):
        if nums[rollingIndex] != 0:
            nums[insertIndex] = nums[rollingIndex]
            insertIndex += 1

    while insertIndex < lenN:
        nums[insertIndex] = 0
        insertIndex += 1


def caterpillarZeroes(nums):
    ZeroIndex = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[ZeroIndex], nums[i] = nums[i], nums[ZeroIndex]
            ZeroIndex += 1
