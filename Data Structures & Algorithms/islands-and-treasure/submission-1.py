class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # DFS min approach
            # start at 0,0
            # search every direction, only if that direction is not -1
            # for each point, we will set our distance to treasuer
                # to the min(curDistance, distanceInOtherDirections)


        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    self.islandsAndTreasaureHelper(grid, y, x, 0)

        # return grid

    def islandsAndTreasaureHelper(self, grid, y, x, curDistance):
        if x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid):
            if grid[y][x] != -1:
                if grid[y][x] >= curDistance:
                        grid[y][x] = curDistance
                        # Keep passing the value along if less than, otherwise do nothing
                        self.islandsAndTreasaureHelper(grid, y - 1, x, curDistance + 1)
                        self.islandsAndTreasaureHelper(grid, y + 1, x, curDistance + 1)
                        self.islandsAndTreasaureHelper(grid, y, x - 1, curDistance + 1)
                        self.islandsAndTreasaureHelper(grid, y, x + 1, curDistance + 1)
                