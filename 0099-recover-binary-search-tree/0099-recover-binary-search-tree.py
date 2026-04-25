# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first = None
        self.middle = None
        self.last = None
        self.prev = TreeNode(float('-inf'))

        def inorder(node):
            if not node:
                return
            
            # Traverse left
            inorder(node.left)

            # Check for violation
            if self.prev and node.val < self.prev.val:
                # First violation
                if not self.first:
                    self.first = self.prev
                    self.middle = node#current
                else:
                    # Second violation
                    self.last = node#current

            # Mark current as previous
            self.prev = node

            # Traverse right
            inorder(node.right)

        inorder(root)

        # Fix swapped nodes
        if self.first and self.last:
            self.first.val, self.last.val = self.last.val, self.first.val
        elif self.first and self.middle:
            self.first.val, self.middle.val = self.middle.val, self.first.val
        """
        Do not return anything, modify root in-place instead.
        """
        