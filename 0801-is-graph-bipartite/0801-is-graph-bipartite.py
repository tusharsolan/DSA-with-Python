from collections import deque
class Solution:
     def isBipartite(self, graph: List[List[int]]) -> bool:

        def dfs(snode, col):
            color[snode] = col

            for nei in graph[snode]:
                if color[nei] == -1:
                    if dfs(nei, 1 - col) == False:
                        return False

                elif col == color[nei]:
                    return False

            return True
        n=len(graph)
        color = [-1] * n

        for i in range(n):
            if color[i] == -1:
                if dfs(i, 0) == False:
                    return False
        return True            
    # def isBipartite(self, graph: List[List[int]]) -> bool:

        
    #     def bfs(snode):
    #         q=deque()
    #         q.append(snode)
    #         color[snode] = 0 
    #         while q:
    #             node=q.popleft()
                 
    #             for nei in graph[node]:
    #                 if color[nei] == -1 :
    #                     color[nei] = 1 -color[node]
    #                     q.append(nei)
    #                 elif color[node] == color[nei] :
    #                     return False  
    #         return True              



    #     n=len(graph)
    #     color=[-1] * n
    #     for i in range(n):
    #         if color[i] == -1 :
    #             if bfs(i) == False :
    #                 return False
    #     return True            

        