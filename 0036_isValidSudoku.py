class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1) need to locate subbox of 3*3 by diving indices by 3 
        # 2) If there is a duplicate integer in row or col or subbox, return zero
        
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        subbox = collections.defaultdict(set)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                    
                elif ((board[r][c] in rows[r]) or 
                     (board[r][c] in cols[c]) or 
                     (board[r][c] in subbox[(r//3,c//3)])):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                subbox[(r//3,c//3)].add(board[r][c])
        return True
    
    # O(n**2), O(1) --> constant values, will not change
