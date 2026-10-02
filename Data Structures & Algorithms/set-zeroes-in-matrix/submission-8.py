class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        zero_row_zero = False
        zero_col_zero = False

        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == 0:
                    # Marking what rows to turn 0
                    if y > 0:
                        matrix[y][0] = 0
                    else:
                        zero_row_zero = True
                    # Marking what cols to turn 0
                    if x > 0:
                        matrix[0][x] = 0
                    else:
                        zero_col_zero = True

        # second time around, here we are turning all corresponding
        # cols and rows from 1 - len() 0, dont want to mess with our
        # first rows or cols, since that could turn the entire spot 0
        # and override our notes we have there

        for y in range(1, len(matrix)):
            for x in range(1, len(matrix[0])):
                if matrix[0][x] == 0 or matrix[y][0] ==0:
                    matrix[y][x] = 0

        #now turn the first col or first row 0 if marked as true
        if zero_row_zero:
            for x in range(len(matrix[0])):
                matrix[0][x] = 0

        if zero_col_zero:
            for y in range(len(matrix)):
                matrix[y][0] = 0
        