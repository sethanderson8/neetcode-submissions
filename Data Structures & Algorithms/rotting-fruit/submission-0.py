class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # Queue of queues for BFS
        toVisit = []
        minDays = 0
        visited = [[False for x in range(len(grid[0]))] for y in range(len(grid))]

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 2:
                    if len(toVisit) == 0:
                        toVisit.append([(y, x)])
                    else:
                        toVisit[0].append((y, x))

        # days = 0 at this point
        minDays = self.daysToRot(grid, toVisit, visited)

        print(grid)

        if self.checkIfFreshFruit(grid):
            return -1
        else:
            return minDays

    def daysToRot(self, grid, toVisit, visited):
        minDays = 0
        while len(toVisit) != 0:
            rotFruitOnDay = False
            curDay = toVisit.pop(0)
            print(curDay)
            nextDay = []
            while len(curDay) != 0:
                curCoord = curDay.pop(0)
                y = curCoord[0]
                x = curCoord[1]
                if x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid)\
                    and not visited[y][x]:
                    visited[y][x] = True
                    if grid[y][x] == 1 or grid[y][x] == 2:
                        # Still need to check around us
                        nextDay.append((y - 1, x))
                        nextDay.append((y + 1, x))
                        nextDay.append((y, x - 1))
                        nextDay.append((y, x + 1))
                        if grid[y][x] == 1:
                            grid[y][x] = 2
                            if not rotFruitOnDay:
                                rotFruitOnDay = True
                                print("Did something")
                                minDays += 1



            if len(nextDay) != 0:
                toVisit.append(nextDay)

        return minDays



    def checkIfFreshFruit(self, grid):
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    return True

        return False
        