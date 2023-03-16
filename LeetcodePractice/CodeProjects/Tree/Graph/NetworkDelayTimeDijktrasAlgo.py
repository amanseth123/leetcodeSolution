class Solution:
    def networkDelayTime3(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))

        dist = {node: float('inf') for node in range(1, N+1)}
        
        def dfs(node, elapsed):
            if elapsed >= dist[node]: #if any new path to node has more elapse time then don't consider and return
                return
            dist[node] = elapsed
            for time, nei in sorted(graph[node]):
                dfs(nei, elapsed + time)
        dfs(K, 0)
        ans = max(dist.values())
        return ans if ans < float('inf') else -1    
    
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #time complexity for djiktra algorithm which uses min Heap is O((E+V)*logV) where E=edges,V=vertices
        graph=defaultdict(list)
        for source,end,time in times:
            graph[source].append((end,time))
        res=0
        level=defaultdict(int)
        visit=set()
        minHeap = [(0,k)]
        count=0
        while minHeap:
            weight,node = heapq.heappop(minHeap)
            if node in visit:
                continue
            res=max(res,weight)
            visit.add(node)
            for nei,w in graph[node]:
                if nei not in visit:
                    heapq.heappush(minHeap,(w+weight,nei))
        return res if len(visit)==n else -1
    
    def networkDelayTime2(self, times: List[List[int]], n: int, k: int) -> int:
        #time complexity for this solution is O(N*E)
        #Each of N nodes can be added to the queue fir all the edges connected to it
        # hence in a complete graph the total number of operations would be N*E and same 
        # goes for space complexity
        graph=defaultdict(list)
        for source,end,time in times:
            graph[source].append((end,time))
        q=[k]
        self.signalReceived=[float('inf')]*(n+1)
        self.signalReceived[k]=0
        while q:
            node = q.pop(0)
            for nde,time in graph[node]:
                arrivalTime = self.signalReceived[node]+time
                if self.signalReceived[nde]>arrivalTime: #if signal received uptill node is better than what already 
                    self.signalReceived[nde]=arrivalTime
                    q.append(nde)
        return max(self.signalReceived[1:]) if max(self.signalReceived[1:])!=float('inf') else -1
        
        # graph=defaultdict(list)
        # for source,end,time in times:
        #     graph[source].append((end,time))
        # res=0
        # level=defaultdict(int)
        # visit=set()
        # minHeap = [(0,k)]
        # count=0
        # while minHeap:
        #     weight,node = heapq.heappop(minHeap)
        #     if node in visit:
        #         continue
        #     res=max(res,weight)
        #     visit.add(node)
        #     for nei,w in graph[node]:
        #         if nei not in visit:
        #             heapq.heappush(minHeap,(w+weight,nei))
        # return res if len(visit)==n else -1
# class Solution(object):
#     def networkDelayTime(self, times, N, K):
#         graph = collections.defaultdict(list)
#         for u, v, w in times:
#             graph[u].append((w, v))

#         dist = {node: float('inf') for node in range(1, N+1)}
        
#         def dfs(node, elapsed):
#             print(node,elapsed,dist)
#             if elapsed >= dist[node]: #if any new path to node has more elapse time then don't consider and return
#                 print("***",dist,elapsed,node)
#                 return
#             dist[node] = elapsed
#             for time, nei in sorted(graph[node]):
#                 dfs(nei, elapsed + time)

#         dfs(K, 0)
#         ans = max(dist.values())
#         return ans if ans < float('inf') else -1
        
        
        
        