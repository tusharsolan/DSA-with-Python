class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        oldcolor = image[sr][sc]
        if oldcolor == color:
            return image
        self.dfs(sr,sc,image,oldcolor,color)
        return image

    def dfs(self,row,col,image,oldcolor,newcolor):
        #out of bounds
        if row < 0 or row>=len(image) or col<0 or col >= len(image[0]):
            return
        # not original color
        if image[row][col] != oldcolor:
            return
        #color already changed
        if image[row][col] == newcolor:
            return
        #change color
        image[row][col] = newcolor
        #go to 4 directions
        self.dfs(row-1,col,image,oldcolor,newcolor)
        self.dfs(row+1,col,image,oldcolor,newcolor)
        self.dfs(row,col-1,image,oldcolor,newcolor)
        self.dfs(row,col+1,image,oldcolor,newcolor)