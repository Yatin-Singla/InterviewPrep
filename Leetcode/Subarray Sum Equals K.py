'''
560. Subarray Sum Equals K
Question: Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example: 
Input:nums = [1,1,1], k = 2
Output: 2
'''


class Solution:
    # partialSumJ - PartialSumI = k -> elements between indices j and i sum to k
    # now we store partialSumI in a hashtable along with the number of times this sum has occured
    # partialSumJ - k = partialSumI
    def subarraySum(self, nums: List[int], k: int) -> int:
        # partial sum = k
        sumDict = {0: 1}
        partialSum, totalCount = 0, 0
        for i in range(len(nums)):
            partialSum += nums[i]
            if partialSum - k in sumDict:
                totalCount += sumDict[partialSum - k]
            if partialSum in sumDict:
                sumDict[partialSum] += 1
            else:
                sumDict[partialSum] = 1
        return totalCount
