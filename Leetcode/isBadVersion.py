class Solution:
    x = [False,False,False,True,True]
    def isBadVersion(self, n):
        return self.x[n-1]

     def firstBadVersion(self, n):
        lower = 1
        upper = n
        while lower < upper:
            middle = int((upper+lower)/2)
            if isBadVersion(middle):
                if middle-1 >= 0:
                    if not isBadVersion(middle-1):
                        return middle
                upper = middle - 1
            else:
                lower = middle + 1

if __name__ == "__main__":
    solution = Solution()
    print(solution.firstBadVersion(5))
