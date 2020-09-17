# Question
# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.

# Example
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


# solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far, maxSum = nums[0], nums[0]
        for i in range(1, len(nums)):
            max_so_far = max(max_so_far + nums[i], nums[i])
            maxSum = max(maxSum, max_so_far)

        return maxSum
