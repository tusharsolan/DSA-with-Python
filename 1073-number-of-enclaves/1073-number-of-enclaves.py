from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        visited=[[False] * m for _ in range(n)]
        q=deque()

        # BFS to mark all land cells reachable from boundary
        for i in range(n):
            for j in range(m):
                # Check if current cell lies on boundary
                if i == 0 or j == 0 or i == n - 1 or j == m - 1:

                    if grid[i][j] == 1 and visited[i][j] == 0 :
                        visited[i][j] = True
                        q.append((i,j))

        # Direction vectors for 4-neighborhood
        delrow = [-1, 0, 1, 0]
        delcol = [0, 1, 0, -1]            

        while q :
            row,col=q.popleft()

            # Explore four directions
            for k in range(4):
                nr=row +delrow[k]
                nc=col +delcol[k]

                # Check bounds, unvisited, and land
                if 0<=nr<n and 0<nc<m and visited[nr][nc] == 0 and grid[nr][nc] == 1:
                    visited[nr][nc] = True
                    q.append((nr,nc))


        # Count land cells that are not visited (i.e., enclaves)
        cnt=0
        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0 and grid[i][j] == 1 :
                    cnt+=1
        return cnt            