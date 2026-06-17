class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # 1.we are given adj matrix - create adj_list out of it
        n = len(isConnected)
        m = len(isConnected[0])
        adj_list =[[] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i!=j and isConnected[i][j]==1:
                    adj_list[i].append(j)
        # 3. traversal - bfs or dfs - just need to update the visisted array
        def dfs(node):
            visited[node] = 1
            for neighbor in adj_list[node]:
                if visited[neighbor] == 0 :
                    dfs(neighbor)
        # 2. count = no of times dfs travesal gone - no of connected components 
        visited= [0]*n
        province_count=0
        for i in range(n):
            if visited[i] == 0 :
                province_count+=1
                dfs(i)

        return province_count                
        

