class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numOfIslands = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    numOfIslands += 1
                    # DFS or BFS to mark down entire island as visited
                    self.searchEntireIsland(grid, y, x)

        return numOfIslands

    def searchEntireIsland(self, grid, y, x):
        if y >= 0 and x >= 0 and x < len(grid[0]) and y < len(grid):
            if grid[y][x] == "1":
                # Mark current Island spot as '0' to denote it has been searched and wont search
                # here again
                grid[y][x] = "0"

                # Need to search up down left and right now
                self.searchEntireIsland(grid, y + 1, x)
                self.searchEntireIsland(grid, y - 1, x)
                self.searchEntireIsland(grid, y, x + 1)
                self.searchEntireIsland(grid, y, x - 1)
        