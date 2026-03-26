# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        pass

    def recursivePostorder(self, root, arr):
        # If the current Tree is NULL (base case for recursion), return
        if root is None:
            return
        
        # Recursively traverse the left subtree
        self.recursivePostorder(root.left, arr)
        
        # Recursively traverse the right subtree
        self.recursivePostorder(root.right, arr)
        
        # Push the current TreeNode's value into the vector
        arr.append(root.val)

    # Function to initiate postorder traversal and return the resulting vector
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Create an empty vector to store postorder traversal values
        arr = []
        
        # Call the postorder traversal function
        self.recursivePostorder(root, arr)
        
        # Return the resulting vector containing postorder traversal values
        return arr