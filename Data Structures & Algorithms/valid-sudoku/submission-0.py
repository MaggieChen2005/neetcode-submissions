class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)   # rows[0] = set of nums seen in row 0
        cols = collections.defaultdict(set)   # cols[0] = set of nums seen in col 0
        boxes = collections.defaultdict(set)  # boxes[(0,0)] = set of nums seen in top-left box

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in boxes[(r // 3, c // 3)]):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])

        return True
