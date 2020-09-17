# Question
# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

class Solution:
    def PascalTriangleRecursive(self, numRows, result):
        if not numRows:
            return
        lengthParentArr = len(result[-1]) if len(result) > 0 else 0
        tempArr = [1]*(lengthParentArr+1)

        for i in range(1, lengthParentArr):
            tempArr[i] = result[-1][i-1] + result[-1][i]

        result.append(tempArr)
        self.PascalTriangleRecursive(numRows-1, result)

    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        self.PascalTriangleRecursive(numRows, result)
        return result


# solution 2

def PascalTriangle(numRows: int):
    if not numRows:
        return []

    result = [[1]]
    for i in range(numRows-1):
        tempArr = (result[i] + [0]) + result[i]
        retulst.append(tempArr)
