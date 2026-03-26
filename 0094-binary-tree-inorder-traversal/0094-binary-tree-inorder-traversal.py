# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        pass

    def recursiveInorder(self, root, arr):
        # If the current Tree is NULL (base case for recursion), return
        if root is None:
            return
        
        # Recursively traverse the left subtree
        self.recursiveInorder(root.left, arr)
        
        # Push the current TreeNode's value into the vector
        arr.append(root.val)
        
        # Recursively traverse the right subtree
        self.recursiveInorder(root.right, arr)

    # Function to initiate inorder traversal and return the resulting vector
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Create an empty vector to store inorder traversal values
        arr = []
        
        # Call the inorder traversal function
        self.recursiveInorder(root, arr)
        
        # Return the resulting vector containing inorder traversal values
        return arr