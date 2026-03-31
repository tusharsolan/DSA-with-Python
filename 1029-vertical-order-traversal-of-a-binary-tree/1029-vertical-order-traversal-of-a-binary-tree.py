from collections import defaultdict, deque
from typing import Optional, List

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        # nodes[x][y] = list of values
        nodes = defaultdict(lambda: defaultdict(list))
        
        # queue: (node, x, y)
        q = deque([(root, 0, 0)])
        
        # BFS traversal
        while q:
            node, x, y = q.popleft()
            
            nodes[x][y].append(node.val)   # â use val
            
            if node.left:
                q.append((node.left, x - 1, y + 1))
            if node.right:
                q.append((node.right, x + 1, y + 1))
        
        # Build result
        ans = []
        for x in sorted(nodes.keys()):
            col = []
            for y in sorted(nodes[x].keys()):
                col.extend(sorted(nodes[x][y]))  # sort values
            ans.append(col)
        
        return ans