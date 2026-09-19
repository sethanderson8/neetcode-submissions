class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Problem
            # Up and left are pacific
            # Down and right are atlantic
            # Need to find all tiles, as [y,x] where water can flow in both oceans

        # Solution
            # BFS in all directions of the coord
            # create two identical grids one for pacific, one for atlantic: boolean
            # Have queue of coords to visit
            # Start with all coord on the border, topleft for pacific, bottomright for atlantic
            # For all those points, if you can reach whatever ocean, mark true on boolean
            # Search all neighbors
                # If neighbors is greater than or = pac/atl touching coord, you know it can reach
                # that ocean. Mark true on corresponding grid. Add neighbors, repeat

            # do this for both oceans, then look at all spots where it is true on both
            # grids

        toVisit = []
        pacific = [[None for x in range(len(heights[0]))] for y in range(len(heights))]
        atlantic = [[None for x in range(len(heights[0]))] for y in range(len(heights))]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for y in range(len(heights)):
            for x in range(len(heights[0])):
                if y == 0 or x == 0:
                    # Mark True for pacific borders
                    toVisit.append((y, x, True, 0))
                if y == len(heights) - 1 or x == len(heights[0]) - 1:
                    # Mark False for atlantic borders
                    toVisit.append((y, x, False, 0))

        dualOceanTiles = []

        self.pacificAtlanticHelper(heights, toVisit, pacific, atlantic, dualOceanTiles, directions)
        print(pacific)
        print(atlantic)
        return dualOceanTiles

    def pacificAtlanticHelper(self, heights, toVisit, pacific, atlantic, dualOceanTiles, directions):
        while len(toVisit) > 0:
            coord = toVisit.pop(0)
            y = coord[0]
            x = coord[1]
            isPacific = coord[2]
            prevHeight = coord[3]



            curOcean = pacific if isPacific else atlantic
            otherOcean = atlantic if isPacific else pacific

            # Only do something if in bounds, and not visited for selected ocean
            if x >= 0 and y >= 0 and x < len(heights[0]) and y < len(heights) and\
                curOcean[y][x] is None:
                # if our current coord, is greater in height, we know it can flow down into the ocean
                # we started from
                if prevHeight <= heights[y][x]:
                    print((y, x))
                    print(heights[y][x])
                    print(prevHeight)
                    curOcean[y][x] = True
                    # Can possibly check other ocean here........
                    if otherOcean[y][x] == True:
                        dualOceanTiles.append((y, x))

                    for dy, dx in directions:
                        toVisit.append((y + dy, x + dx, isPacific, heights[y][x]))

