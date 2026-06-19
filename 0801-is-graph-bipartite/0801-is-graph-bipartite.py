from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def bfs(snode):
            q=deque()
            q.append(snode)
            color[snode] = 0 
            while q:
                node=q.popleft()
                 
                for nei in graph[node]:
                    if color[nei] == -1 :
                        color[nei] = 1 -color[node]
                        q.append(nei)
                    elif color[node] == color[nei] :
                        return False  
            return True              



        n=len(graph)
        color=[-1] * n
        for i in range(n):
            if color[i] == -1 :
                if bfs(i) == False :
                    return False
        return True            

        