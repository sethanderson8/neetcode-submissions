class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = []
        visited = [[False for x in range(len(grid[0]))] for y in range(len(grid))]
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    queue.append((y, x))

        while len(queue) != 0:
            nextCoord = queue.pop(0)
            print(nextCoord)
            y = nextCoord[0]
            x = nextCoord[1]
            curDistance = grid[y][x]
            visited[y][x] = True
            self.islandsAndTreasaureHelper(grid, y - 1, x, queue, curDistance + 1, visited)
            self.islandsAndTreasaureHelper(grid, y + 1, x, queue, curDistance + 1, visited)
            self.islandsAndTreasaureHelper(grid, y, x - 1, queue, curDistance + 1, visited)
            self.islandsAndTreasaureHelper(grid, y, x + 1, queue, curDistance + 1, visited)


    def islandsAndTreasaureHelper(self, grid, y, x, queue, curDistance, visited):
        if x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid):
            if grid[y][x] != -1 and not visited[y][x]:
                grid[y][x] = curDistance
                visited[y][x] = True
                queue.append((y, x))

                