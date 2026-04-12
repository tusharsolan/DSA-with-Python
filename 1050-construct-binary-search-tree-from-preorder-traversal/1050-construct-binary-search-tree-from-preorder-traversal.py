# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        i = [0]   # use list to make it mutable
        
        def build(bound):
            # Base case
            if i[0] == len(preorder) or preorder[i[0]] > bound:
                return None
            
            # Create root
            root = TreeNode(preorder[i[0]])
            i[0] += 1
            
            # Build left and right subtree
            root.left = build(root.val)
            root.right = build(bound)
            
            return root
        
        return build(float('inf'))