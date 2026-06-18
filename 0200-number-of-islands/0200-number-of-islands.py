from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(row,col):
            vis[row][col] =1
            q=deque()
            q.append((row,col))

            while q :
                r,c=q.popleft()

                directions = [(1,0), (-1,0), (0,1), (0,-1)]

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if ( nr>=0 and nr<n) and (nc>=0 and nc<m) and   not vis[nr][nc] and grid[nr][nc] =='1':
                        vis[nr][nc] =1
                        q.append((nr,nc))


        n=len(grid)
        m=len(grid[0])
        vis=[[0 for j in range(m)]for i in range(n)]
        cnt=0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and not  vis[i][j]:
                    cnt+=1
                    bfs(i,j)
        return cnt

        