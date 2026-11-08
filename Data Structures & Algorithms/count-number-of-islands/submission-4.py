class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen_land = set()
        num_of_islands = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == '1' and (y, x) not in seen_land:
                    num_of_islands += 1
                    # unseen land, go explore entire island now and mark each
                    # piece of connected land as seen in the set
                    self.explore_island(grid, seen_land, y, x)

        return num_of_islands

    def explore_island(self, grid, seen_land, y, x):
        # make sure it is in bounds, we have not seen this land before, and we are only exploring
        # land
        if (y >= 0 and y < len(grid) and x >= 0 and x < len(grid[0]) and (y, x) not in seen_land
            and grid[y][x] == '1'):
            # first add to the set
            seen_land.add((y, x))
            # then explore/recurse all 4 directions
            self.explore_island(grid, seen_land, y+1, x)
            self.explore_island(grid, seen_land, y-1, x)
            self.explore_island(grid, seen_land, y, x+1)
            self.explore_island(grid, seen_land, y, x-1)
