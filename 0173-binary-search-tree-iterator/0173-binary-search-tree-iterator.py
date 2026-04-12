# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.pushAll(root)

    # Return True if next smallest exists
    def hasNext(self) -> bool:
        return len(self.stack) > 0

    # Return next smallest number
    def next(self) -> int:
        node = self.stack.pop()
        self.pushAll(node.right)
        return node.val

    # Helper function to push all left nodes
    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node = node.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()