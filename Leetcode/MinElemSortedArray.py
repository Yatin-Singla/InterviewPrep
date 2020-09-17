# Question : 153. Find Minimum in Rotated Sorted Array
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# Find the minimum element.
# * assumption: You may assume no duplicate exists in the array.
# * Example 1:
# Input: [3,4,5,1,2]
# Output: 1
# * Example 2:
# Input: [4,5,6,7,0,1,2]
# Output: 0

def findMin(nums):
    if not nums:
        return 0
    compareElement, low, high = nums[0], 0, len(nums) - 1
    if nums[high] > nums[low]:
        return nums[low]
    while low <= high:
        mid = (low+high)//2

        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        if nums[mid - 1] > nums[mid]:
            return nums[mid]

        if nums[mid] < compareElement:
            high = mid-1
        else:  # nums[mid] > CompareElement
            low = mid+1

    return nums[mid]


if __name__ == "__main__":
    input1 = [3, 1, 2]
    print(findMin(input1))
