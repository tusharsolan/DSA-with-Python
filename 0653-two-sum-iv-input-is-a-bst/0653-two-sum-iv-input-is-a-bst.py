# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
         # If root is None, tree is empty, return False
        if not root:
            return False

        # Create two iterators: one from smallest, one from largest
        l = BSTIterator(root, False)# for next()
        r = BSTIterator(root, True)# for before()

        # Get first values
        i = l.next()
        j = r.next()#r.before()

        # Loop until two values meet
        while i < j:
            # If sum is exactly k, return True
            if i + j == k:
                return True
            # If sum is smaller, move left iterator
            elif i + j < k:
                i = l.next()
            # If sum is larger, move right iterator
            else:
                j = r.next()
        # If no pair found, return False
        return False


# This class is an iterator for traversing the BST
class BSTIterator:
    # Constructor initializes the iterator with root and traversal direction
    def __init__(self, root, isReverse):
        # A stack is used to store nodes while traversing
        self.stack = []
        # This flag tells whether we are doing normal inorder or reverse inorder
        self.reverse = isReverse
        # Push all nodes on one side into the stack
        self.pushAll(root)

    # This function checks if more nodes are left
    def hasNext(self):
        # If stack has elements, then nodes are still left
        return len(self.stack) > 0

    # This function returns the next node value in chosen order
    def next(self):
        # Pop the top node from stack
        tmpNode = self.stack.pop()
        # If reverse is False, move to right child
        if not self.reverse:
            self.pushAll(tmpNode.right)
        # If reverse is True, move to left child
        else:
            self.pushAll(tmpNode.left)
        # Return the value of node processed
        return tmpNode.val

    # Helper function to push nodes from current node down to left or right edge
    def pushAll(self, node):
        # Keep looping until node becomes None
        while node:
            # Add current node to stack
            self.stack.append(node)
            # If reverse is True, go to right child
            if self.reverse:
                node = node.right
            # Otherwise, go to left child
            else:
                node = node.left
        