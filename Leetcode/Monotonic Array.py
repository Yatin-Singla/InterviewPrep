class Solution:
    def monotonicInc(self, A):
        length = len(A)
        if length < 2:
            return True
        for i in range(1, length):
            if (A[i] - A[i-1]) < 0:
                return False
        return True
            
    def monotonicDec(self, A):
        length = len(A)
        if length < 2:
            return True
        for i in range(1, length):
            if (A[i] - A[i-1]) > 0:
                return False
        return True
        
    def isMonotonic(self, A: List[int]) -> bool:
        return self.monotonicInc(A) or self.monotonicDec(A)