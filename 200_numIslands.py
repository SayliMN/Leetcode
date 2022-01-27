def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i,j,grid):
            q = deque()
            q.append((i,j))
            while q:
                x,y = q.popleft()
                dirs = [[1,0],[0,1],[0,-1],[-1,0]]
                for dx, dy in dirs:
                    xx = dx + x
                    yy = dy + y
                    if 0<=xx<m and 0<=yy<n and grid[xx][yy] == '1':
                        q.append((xx,yy))
                        grid[xx][yy] = 'X'
                       
                        
        island = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i,j,grid)
                    island += 1
        return island
      
#       Time complexity: O(M*N)
#       Space complexity: O(M*N)
