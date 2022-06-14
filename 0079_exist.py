class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if (r < 0 or c < 0 or r >= rows or c >= cols or
               board[r][c] != word[i] or (r,c) in path):
                    return False
            
            path.add((r,c))
            result = (dfs(r, c+1, i+1) or
                      dfs(r+1, c, i+1) or
                      dfs(r, c-1, i+1) or
                      dfs(r-1, c, i+1))
            path.remove((r,c))
            return result
            
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0): return True
            
        return False
    
    # O(n*m*dfs*length(word)) --> (n*m*4*L), O(L)
 
                    
