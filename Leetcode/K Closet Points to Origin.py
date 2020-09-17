import heapq


class Solution:
    def kClosest(self, points, K: int):
        return heapq.nlargest(K, points, key=lambda x: x[0]*x[0] + x[1]*x[1])


if __name__ == "__main__":
    points = [[1, 3], [-2, 2]]
    K = 1
    answer = Solution()
    print(answer.kClosest(points, K))
