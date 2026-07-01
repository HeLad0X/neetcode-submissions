class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = {}
        col_map = {}
        square_map = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                curr = board[i][j]
                if curr == ".":
                    continue
                
                if i in row_map:
                    if curr in row_map[i]: return False
                    row_map[i][curr] = 1
                else:
                    row_map[i] = dict()
                    row_map[i][curr] = 1

                if j in col_map:
                    if curr in col_map[j]: return False
                    col_map[j][curr] = 1
                else:
                    col_map[j] = dict()
                    col_map[j][curr] = 1

                sq_idx = (i // 3) * 3 + (j // 3)
                if sq_idx in square_map:
                    if curr in square_map[sq_idx]: return False
                    square_map[sq_idx][curr] = 1
                else:
                    square_map[sq_idx] = dict()
                    square_map[sq_idx][curr] = 1

        
        return True