class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Search until we find an 'O'
        # Once we find an 'O', we will dfs its neighbors.
        # If neighbor is 'X', do nothin
        # If neighbor is 'O' and touches border, return False, do not fill!
            # if neighbor is 'O' and does not touch border, return True and search neighbors

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == "O" and (x == 0 or y == 0 or x == len(board[0]) - 1\
                    or y == len(board) - 1):
                    # Filling all non fillable Os with Ts
                    self.filler(board, y, x, directions, "O", "T")
        
        print(board)


        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == "O":
                    # Filling all Os left with Xs
                    self.filler(board, y, x, directions, "O", "X")

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == "T":
                    # Filling all Ts with Os
                    self.filler(board, y, x, directions, "T", "O")

    def filler(self, board, y, x, directions, charToFill, charFiller):
        if x >= 0 and y >= 0 and x < len(board[0]) and y < len(board) and\
            board[y][x] == charToFill:
            print(y,x)
            # visited[y][x] = True
            board[y][x] = charFiller
            for dy, dx in directions:
                self.filler(board, y + dy, x + dx, directions, charToFill, charFiller)
