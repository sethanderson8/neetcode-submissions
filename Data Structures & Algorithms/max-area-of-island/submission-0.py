class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxIslandArea = 0
        
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    maxIslandArea = max(maxIslandArea, self.getIslandArea(grid, y, x))

        return maxIslandArea

    def getIslandArea(self, grid, y, x):
        if y >= 0 and x >= 0 and y < len(grid) and x < len(grid[0]):
            if grid[y][x] == 1:
                # Marking area as searched and incredmenting area for this spot
                grid[y][x] = 0
                return 1 + \
                    self.getIslandArea(grid, y + 1, x) + \
                    self.getIslandArea(grid, y - 1, x) + \
                    self.getIslandArea(grid, y, x + 1) + \
                    self.getIslandArea(grid, y, x - 1)
            else:
                return 0
        else:
            return 0
        