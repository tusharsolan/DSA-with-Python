class Solution:
    # Helper function to find the index of the row 
    # with the maximum element in a given column
    def maxElement(self,mat,col):
        m=len(mat)
        max_value = float('-inf')
        index=-1

        # Iterate through each row to find the maximum element 
        # in the specified column
        for i in range(m):
            if mat[i][col] >max_value:
                max_value =mat[i][col]
                index= i
        return index    

    # Function to find a peak element in the 2D matrix 
    # using binary search 
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m=len(mat)
        n=len(mat[0])
        
        # Initialize the lower and upper bounds for binary search
        low =0
        high=n-1

        while low <=high:
            mid=(low+high) // 2

            # Find the index of the row with the maximum element 
            # in the middle column
            row = self.maxElement(mat,mid)

            # Determine the elements to the left and right of 
            # the middle element in the found row
            left=mat[row][mid-1] if mid - 1 >=0 else float('-inf')
            right=mat[row][mid+1] if mid +1 < n else float('-inf')

            # Check if the middle element is greater than its neighbors
            if mat[row][mid] > left and mat[row][mid] >right:
                return [row,mid]
            elif left > mat[row][mid]:
                high=mid-1
            else:
                low=mid+1        