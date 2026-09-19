class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Rows and colums needs to have digits between 1-9, no duplicates
            # Maybe use set for this
        # Each 9x9 grid must have digits 1-9

        rows = [set() for i in range(len(board))]
        columns = [set() for i in range(len(board[0]))]
        grids = [set() for i in range(len(board))]

        # First verify rows, then columns, then rows, then grids

        # Time complexity is (3n)
        # Space complexity is (3n)

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x].isdigit():
                    print(rows[y])
                    # print(board[y][x])
                    print(y)
                    # Row Checking
                    if board[y][x] in rows[y]:
                        print("here1")
                        return False
                    
                    # Column checking
                    if board[y][x] in columns[x]:
                        print("here2")
                        return False

                    # Grid checking
                    if board[y][x] in grids[(x // 3) + (y // 3  * 3)]:
                        print("here3")
                        return False

                    # Add value to each set now
                    grids[x // 3 + y // 3].add(board[y][x])
                    columns[x].add(board[y][x])
                    rows[y].add(board[y][x])

        return True
