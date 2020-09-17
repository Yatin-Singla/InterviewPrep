# * Question:
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
# * Example 1:
# Input: [3,0,1]
# Output: 2
# * Example 2:
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# * Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

# Gauss theorem -> sum of first N numbers
def missingNumber(self, nums: List[int]) -> int:
    if not nums:
        return 0
    lenN = len(nums)
    expectedSum = (lenN)*(lenN+1)/2
    actualSum = sum(nums)

    return int(expectedSum)-actualSum
