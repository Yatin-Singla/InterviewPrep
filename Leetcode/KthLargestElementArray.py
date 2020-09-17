# Question: 215. Kth Largest Element in an Array
# Find the kth largest element in an unsorted array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# * Example 1:
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# * Example 2:
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# * Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.

# solution

def findKthLargest(nums, k):
    lenNums = len(nums)
    if lenNums == 1:
        return nums[0]
    kLargest = []
    largestNumber = nums[0]
    sizeKArray = lenNums//2
    for i in range(1, len(nums)):
        if i % sizeKArray == 0:
            kLargest.append(largestNumber)
            largestNumber = nums[i]
        elif nums[i] > largestNumber:
            largestNumber = nums[i]

    kLargest.append(largestNumber)
    smallest = kLargest[0]
    # find the smallest
    for i in range(1, len(kLargest)):
        if kLargest[i] < smallest:
            smallest = kLargest[i]
    return smallest


if __name__ == "__main__":
    input1 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    print(findKthLargest(input1, 4))
