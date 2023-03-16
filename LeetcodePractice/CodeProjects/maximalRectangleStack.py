class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def MaximumArea(heights): #largest rectangle in a histogram
            stack=[]
            maxArea = 0
            for i,h in enumerate(heights):
                start=i
                while stack and stack[-1][1]>h:
                    index,height = stack.pop()
                    maxArea = max(maxArea,height*(i-index))
                    start=index
                stack.append((start,h))
            for i,h in stack:
                maxArea = max(maxArea,h*(len(heights)-i))
            return maxArea
            
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j]=int(matrix[i][j])

        res=0
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i-1][j]==1 or (matrix[i-1][j])>1:
                    if int(matrix[i][j])!=0:
                        matrix[i][j]=(matrix[i][j])+(matrix[i-1][j])
        for i in range(len(matrix)):
            ans=MaximumArea(matrix[i])
            res=max(ans,res)
        return res
        
        
        
        
        
        
        
        