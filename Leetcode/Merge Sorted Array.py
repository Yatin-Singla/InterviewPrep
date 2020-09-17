class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = 0
        begPtr1 = begPtr2 = 0
        tempNums1 = nums1[:m]
        while begPtr1 < m and begPtr2 < n:
            if tempNums1[begPtr1] < nums2[begPtr2]:
                nums1[index] = tempNums1[begPtr1]
                begPtr1 += 1
            else:
                nums1[index] = nums2[begPtr2]
                begPtr2 += 1
            index += 1
        
        if begPtr1 != m:
            nums1[index:] = tempNums1[begPtr1:m]
        else:
            nums1[index:] = nums2[begPtr2:n]
            
        return nums1
                