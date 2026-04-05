# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
         # If tree is empty, return 0
        if root is None:
            return 0
        # List used to pass count by reference
        count = [0]
        # Perform inorder traversal to count nodes
        self.inorder(root, count)
        # Return total count
        return count[0]
         # Helper function to count nodes using inorder traversal
    def inorder(self, root, count):
        # If node is None, stop recursion
        if root is None:
            return
        # Increment count for current node
        count[0] += 1
        # Recursively count nodes in left subtree
        self.inorder(root.left, count)
        # Recursively count nodes in right subtree
        self.inorder(root.right, count)

    
        