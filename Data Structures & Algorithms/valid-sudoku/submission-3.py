class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        min_grid_set = [set() for i in range(9)]
        row_set = [set() for i in range(9)]
        col_set = [set() for i in range(9)]

        # Idea is that for this, you go through each num, and check the corresponding set
        # for it, to see whether or not there are duplicates. As soon as there is a duplicate
        # in any of the sets, you can return False since it is not valid
        # easy to figure out the set for the row and col because that corresponding to the
        # y and x on the 2x2 matrix
        # To figre out the grid index we are checking, we would do [col // 3 + row // 3 * 3]
            # To test, [5,2] = [1 + 0] = 1, 
            # next row [5, 4] = [1 + 3] = 4
            # Last row, last grid [8,8] = [2 + 2 * 3 (6)] = 8

        for col in range(len(board)):
            for row in range(len(board[0])):
                cur_val = board[col][row]
                if cur_val.isalnum():
                    if (cur_val in min_grid_set[col // 3 + row // 3 * 3] or
                        cur_val in row_set[row] or cur_val in col_set[col]):
                        return False
                    else:
                        min_grid_set[col // 3 + row // 3 * 3].add(cur_val)
                        row_set[row].add(cur_val)
                        col_set[col].add(cur_val)

        return True