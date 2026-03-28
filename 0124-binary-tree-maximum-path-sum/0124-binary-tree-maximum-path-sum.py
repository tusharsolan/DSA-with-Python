# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        self.dfs(root)
        return self.max_sum

    # Recursive DFS helper
    def dfs(self, node):
        if not node:
            return 0

        # Recursively find left and right max path sum
        left = max(0, self.dfs(node.left))
        right = max(0, self.dfs(node.right))

        # Update max sum if path through node is better
        self.max_sum = max(
            self.max_sum,
            left + right + node.val
        )

        # Return one-sided path
        return max(left, right) + node.val

'''
class Solution:
    def maxPathSum(self, root):
        # Initialize global maximum path sum
        max_sum = float('-inf')
        
        # DFS helper function
        def dfs(node):
            nonlocal max_sum  # allows us to modify max_sum inside this function
            
            # Base case: if node is None, return 0
            if not node:
                return 0
            
            # Recursively get max path sum from left and right subtree
            # Ignore negative paths by taking max with 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            
            # Calculate path sum passing through current node
            # (this is the "full path" including both sides)
            current_sum = left + right + node.val
            
            # Update global maximum if current path is better
            max_sum = max(max_sum, current_sum)
            
            # Return the maximum one-sided path (either left or right)
            # This is used by parent nodes
            return max(left, right) + node.val
        
        # Start DFS traversal from root
        dfs(root)
        
        # Return the maximum path sum found
        return max_sum        
        '''