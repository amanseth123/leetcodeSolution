class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights)==0:
            return 0
        stack=[] #pair of index and height
        maxArea = 0
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1]>h: #stack[-1][1] larger value and can't be extended to right of i
                index,height = stack.pop() # pop because it can't be extended now
                print(height,i,index,start,maxArea,stack)
                maxArea = max(maxArea,height*(i-index)) # calculate max Area, height=height of the largest histogram not the smaller one 
                start = index #set the start pointer to index to calculate the width
            print("check")
            stack.append((start,h))
        print(stack)
        for i,h in stack:
            maxArea = max(maxArea,h*(len(heights)-i)) # we're sure that the right of i is always greater than h
        return maxArea
        

        