class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True        
        low = 0
        high = len(s) - 1
        while low < high: 
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return s[low:high] == s[low:high][::-1] or s[low+1:high+1] == s[low+1:high+1][::-1]
            
        return True