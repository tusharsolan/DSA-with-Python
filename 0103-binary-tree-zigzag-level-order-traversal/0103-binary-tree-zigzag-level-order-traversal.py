# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # List to store the final zigzag traversal result
        result = []

        # If tree is empty, return empty list
        if not root:
            return result

        # Queue for BFS traversal
        q = deque([root])

        # Boolean flag to control traversal direction
        leftToRight = True

        # Loop until all levels are processed
        while q:
            # Get the number of nodes at the current level
            size = len(q)

            # Temporary list to store current level's values
            level = [0] * size

            # Process each node in the current level
            for i in range(size):
                # Get the front node from queue
                node = q.popleft()

                # Determine index where this value should be stored
                #if True (index=i) and else false means size-1-i  
                index = i if leftToRight else size - 1 - i
                level[index] = node.val

                # Add left child to queue if it exists
                if node.left:
                    q.append(node.left)
                # Add right child to queue if it exists
                if node.right:
                    q.append(node.right)

            # Flip direction for the next level
            leftToRight = not leftToRight

            # Add current level to result
            result.append(level)

        # Return zigzag traversal result
        return result