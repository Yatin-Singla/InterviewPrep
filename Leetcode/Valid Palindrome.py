class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True
        
        tempS = s.lower()
        Answer = []
        for char in tempS:
            if char.isalnum():
                Answer.append(char)
            
        return Answer == Answer[::-1]