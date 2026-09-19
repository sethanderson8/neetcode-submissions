class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numOfIslands = 0

        # full grid of -1 to track where I have visited to not repeat visit islands

        hasVisited = [["-1" for x in range(len(grid[0]))] for y in range(len(grid))]

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                # We have not visited there yet
                if hasVisited[y][x] == "-1":
                    # We see an island
                    if grid[y][x] == "1":
                        numOfIslands += 1
                        # DFS or BFS to mark down entire island as visited
                        self.searchEntireIsland(grid, hasVisited, y, x)
                    else:
                        # It is ocean, mark as visited
                        hasVisited[y][x] = "0"

        return numOfIslands

    def searchEntireIsland(self, grid, hasVisited, y, x):
        if y >= 0 and x >= 0 and x < len(grid[0]) and y < len(grid):
            if grid[y][x] == "1" and hasVisited[y][x] == "-1":
                # Marking this spot on the island as 0
                hasVisited[y][x] = "0"

                # Need to search up down left and right now
                self.searchEntireIsland(grid, hasVisited, y + 1, x)
                self.searchEntireIsland(grid, hasVisited, y - 1, x)
                self.searchEntireIsland(grid, hasVisited, y, x + 1)
                self.searchEntireIsland(grid, hasVisited, y, x - 1)
        