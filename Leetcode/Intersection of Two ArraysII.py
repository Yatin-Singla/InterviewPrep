class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashtable = {}
        HT = {}
        result = []
        for i in nums1:
            if i in hashtable.keys():
                hashtable[i] += 1
            else:
                hashtable[i] = 1
                
        for i in nums2:
            if i in HT.keys():
                HT[i] += 1
            else:
                HT[i] = 1
        
        for key,values in hashtable.items():
            if key in HT.keys():
                for i in range(min(HT[key],values)):
                    result.append(key)
                
        return result
        