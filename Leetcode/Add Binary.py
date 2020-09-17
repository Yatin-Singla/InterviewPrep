class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = 0
        dictionary = {str(key):key for key in range(10)}
        L1 = len(num1)
        L2 = len(num2)

        for i in range(L1-1,-1,-1):
            result += dictionary[num1[i]]*pow(10,L1-1-i)
        for i in range(L2-1,-1,-1):
            result += dictionary[num2[i]]*(10^(L2-1-i))
            
        return str(result)

if __name__ == "__main__":
    sol = Solution()
    print(sol.addStrings("1","1"))        