class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.uniquePathsHelper(0, 0, m, n)
        
    def uniquePathsHelper(self, x, y, m, n):
        if x == m - 1 and y == n - 1:
            return 1
        elif x >= m or y >= n:
            return 0
        else:
            return self.uniquePathsHelper(x + 1, y, m, n) + \
                self.uniquePathsHelper(x, y + 1, m, n)
