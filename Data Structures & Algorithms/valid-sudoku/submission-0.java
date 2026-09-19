class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer, Set<Character>> columnMap = new HashMap<>();

        // Condition that indicate non valid board:
        // Repeating numbers in a row or column
        // Repeating numbers in a 3x3 square
        for (int i = 0; i < board.length; i++) {
            Set<Character> rowSet = new TreeSet<>();
            for (int j = 0; j < board[i].length; j++) {
                // Column checking
                if (columnMap.get(j) == null) {
                    // Create new unique set for each column
                    columnMap.put(j, new TreeSet<Character>());
                }
                if (columnMap.get(j).contains(board[i][j])) {
                    return false;
                } else if(board[i][j] != '.') {
                    columnMap.get(j).add(board[i][j]);
                }

                // Row checking
                if (rowSet.contains(board[i][j])) {
                    return false;
                } else if(board[i][j] != '.') {
                    rowSet.add(board[i][j]);
                }

                // Small square checking
                if ((i == 0 || i == 3 || i ==6) && (j == 0 || j == 3 || j == 6)) {
                    Set<Character> squareSet = new TreeSet<>();
                    for (int x = i; x < i + 3; x ++) {
                        for (int y = j; y < j + 3; y ++) {
                            if (squareSet.contains(board[x][y])) {
                                return false;
                            } else if(board[x][y] != '.') {
                               squareSet.add(board[x][y]);
                            }
                        }
                    }
                }
            }
        }

        return true;
    }
}
