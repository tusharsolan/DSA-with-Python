# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        
        curr = root.val
        
        # If both nodes are greater â go right
        if curr < p.val and curr < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # If both nodes are smaller â go left
        if curr > p.val and curr > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # Otherwise, this is the split point (LCA)
        return root
        