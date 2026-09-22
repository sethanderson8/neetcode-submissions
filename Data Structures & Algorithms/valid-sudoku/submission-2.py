class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # base case, if there is a duplicate in row, column for 3x3 square, false
        # default case is true 

        # these are the check sets, each time we encounter a digit
        # add it here for the corresponds x, y, or board (1-9)
        # If there is a duplicate in said row, column or grid, return
        # false right away
        rows = [set() for i in range(len(board))]
        columns = [set() for i in range(len(board[0]))]
        grids = [set() for i in range(len(board))]

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x].isdigit():
                    # Row Checking
                    if board[y][x] in rows[y]:
                        return False
                    
                    # Column checking
                    if board[y][x] in columns[x]:
                        return False

                    # 3x3 Grid checking. We are doing floor division here
                    if board[y][x] in grids[(x // 3) + (y // 3)  * 3]:
                        return False

                    rows[y].add(board[y][x])
                    columns[x].add(board[y][x])
                    grids[(x // 3) + (y // 3) * 3].add(board[y][x])
                        

        return True
