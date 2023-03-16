
class MedianFinder:
    # using heap, pop and push takes logn time 
    def __init__(self):
        #small --> a large Heap and large--> minHeap because we want every element in small
        # to be less than every element in large so small maxHeap will give the largest value in small to compare with the smallest value from the minHeap(large)
        self.small,self.large=[],[]
        

    def addNum(self, num: int) -> None: # O(logn)
        heapq.heappush(self.small,-1*num)# default adding to small and converting defaultminHeap to maxHeap by multiplying -1
        if (self.small and self.large and (-1*self.small[0])>self.large[0]): # every element of small should be less than every element in large so pop from small if there is an element greater than any element in large
            val = -1*heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        if len(self.large)>len(self.small)+1: # if len(large)-len(small)>1 then pop from self.large and push in self.small
            val = heapq.heappop(self.large)
            heapq.heappush(self.small,-1*val)
        if len(self.large)+1<len(self.small):# if len(small)-len(large)>1 then pop from self.small and push in self.large
            val = heapq.heappop(self.small)
            heapq.heappush(self.large,-1*val)
        
        
    def findMedian(self) -> float:
        
        if len(self.small)>len(self.large): # odd Length with odd value in self.small
            return -1*self.small[0]
        if len(self.large)>len(self.small): # odd length with odd value in self.large
            return self.large[0]
        return (((-1*self.small[0])+self.large[0])/2) # even length

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()