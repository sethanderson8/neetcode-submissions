class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Try using the 0 column and 0 x to make which cols and rows to turn to 0
        # loop through entire array marking this the first time
        # if any of the first x or y are 0 have a boolean for it so you can then change
        # it to zero 0, but rn we are using it to record what other cols and rows to turn to
        # 0
        # once done iterating, iterate over all the first y, if any are 0, mark that entire x 0
        # iterate over first x, if any are 0, mark entire y as 0
        # finally is first y or first x had 0s, then iterate over those respectively and turn them 0
        row_zero_zero = False
        col_zero_zero = False
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == 0:
                    if x > 0:
                        matrix[0][x] = 0
                    else:
                        col_zero_zero = True
                    if y > 0:
                        matrix[y][0] = 0
                    else:
                        row_zero_zero = True

        for y in range(1, len(matrix)):
            if matrix[y][0] == 0:
                # here we are now turning that entire row 0
                for x in range(1, len(matrix[0])):
                    matrix[y][x] = 0

        for x in range(1, len(matrix[0])):
            if matrix[0][x] == 0:
                # here we are now turning that entire col 0
                for y in range(1, len(matrix)):
                    matrix[y][x] = 0

        if row_zero_zero:
            for x in range(len(matrix[0])):
                matrix[0][x] = 0

        if col_zero_zero:
            for y in range(len(matrix)):
                matrix[y][0] = 0
