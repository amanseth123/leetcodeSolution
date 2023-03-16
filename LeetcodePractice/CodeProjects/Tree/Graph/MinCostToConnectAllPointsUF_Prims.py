class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        adj = {i:[] for i in range(n)}
        def getDist(p1,p2):
            return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
        for i in range(n):
            for j in range(i+1,n):
                dist = getDist(points[i],points[j])
                adj[i].append((dist,j))
                adj[j].append((dist,i))
        #prim's algorithm
        minHeap = [(0,0)]
        visit=set()
        total_cost=0
        while minHeap:
            dist,i = heapq.heappop(minHeap)
            if i in visit:
                continue 
            total_cost += dist
            visit.add(i)
            for new_dis,nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minHeap,(new_dis,nei))
        return total_cost # time complexity: O((V+E)*logV)
    # V+E standard bfs * logV for each heap push operation
    def minCostConnectPoints2(self, points: List[List[int]]) -> int:
        n=len(points)
        parents=list(range(n))
        def find(x):  #O(logn)
            if parents[x]!=x:
                parents[x]=find(parents[x])
            return parents[x]
    
        def union(x1,x2): #O(1)
            r1,r2 = find(x1),find(x2)
            if r1!=r2:
                parents[r2]=r1
                return True
            else:
                return False
        paths=[]
        
        def getDist(p1,p2):
            return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
        for i in range(n):
            for j in range(i+1,n):
                dist = getDist(points[i],points[j])
                paths.append((dist,i,j))
        paths.sort()
        print(paths)
        
        ans=0
        for dist,p1,p2 in paths:#O(n=len(edges))
            if union(p1,p2):
                ans+=dist
        return ans
                    
        