class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n=len(board)
        m=len(board[0])
        if n == 0 or m == 0:
            return 
        visited=[[0]*m for _ in range(n)]

        def dfs(r,c):
            visited[r][c] = 1
            dr,dc=[-1,0,1,0],[0,1,0,-1]

            for k in range(4):
                nr,nc = r+dr[k], c+dc[k]

                if 0<=nr<n and  0<=nc<m and visited[nr][nc] ==0 and  board[nr][nc] == 'O':
                    dfs(nr,nc)

        #row
        # visted=[0*m for _ in range(n)]
        for j in range(m):
            if visited[0][j] == 0 and board[0][j] == 'O':
                dfs(0,j)
            if visited[n-1][j] == 0 and board[n-1][j] == 'O':
                dfs(n-1,j)
                
        #col
        for i in range(n):
            if visited[i][0] == 0  and board[i][0] == 'O':
                dfs(i,0)
            if visited[i][m-1] == 0 and board[i][m-1] == 'O':
                dfs(i,m-1)    

        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0 and board[i][j] == 'O':
                    board[i][j] = 'X'
        return board            