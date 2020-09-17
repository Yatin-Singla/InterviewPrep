# Question:
# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.

# Example:
""" 
@param example 1
Input: [3,2,3]
Output: 3
"""

"""
@param example 2
Input: [2,2,1,1,1,2,2]
Output: 2
"""

# Solution

"""@param solution 1"""


def majElem(nums: List[int]) -> int:
    nums.sort()
    return nums[len(nums) // 2]


"""@param solution 2"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lenN, hashT = len(nums), {}
        if lenN == 1:
            return nums[0]
        for item in nums:
            if item in hashT:
                hashT[item] += 1
                if hashT[item] > lenN // 2:
                    return item
            else:
                hashT[item] = 1
