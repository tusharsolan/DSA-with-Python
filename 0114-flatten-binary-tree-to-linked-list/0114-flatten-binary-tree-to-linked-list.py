# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        # return if node is null
        if root is None:
            return
        # flatten right subtree first
        self.flatten(root.right)
        # flatten left subtree next
        self.flatten(root.left)
        # connect current node's right to previously processed node
        root.right = self.prev
        # nullify left pointer
        root.left = None
        # update previous to current
        self.prev = root

    # initialize previous node reference
    def __init__(self):
        self.prev = None
        
        """
        Do not return anything, modify root in-place instead.
        """
        