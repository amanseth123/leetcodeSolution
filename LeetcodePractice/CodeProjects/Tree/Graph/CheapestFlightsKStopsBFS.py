import heapq
from queue import PriorityQueue

def build_graph(n, flights):
    graph = [[] for _ in range(n)]
    for src, dst, price in flights:
        graph[src].append((dst, price))
    return graph

class Solution:
    def findCheapestPrice2(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = build_graph(n, flights)
        q = [(0, src, 0)]
        #q=PriorityQueue()
        #q.put((0,src,0))
        while q:
            cost, city, stops = heapq.heappop(q)
            #cost,city,stops=q.get()
            if city == dst:
                return cost
            if stops > K:
                continue
            for neighbor, price in graph[city]:
                #q.put((cost+price,neighbor,stops+1))
                heapq.heappush(q, (cost + price, neighbor, stops + 1))
        return -1
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = build_graph(n, flights)
        #q = [(0, src, 0)]
        q=PriorityQueue()
        q.put((0,src,0))
        while not q.empty():
            #cost, city, stops = heapq.heappop(q)
            cost,city,stops=q.get()
            if city == dst:
                return cost
            if stops > K:
                continue
            for neighbor, price in graph[city]:
                q.put((cost+price,neighbor,stops+1))
                #heapq.heappush(q, (cost + price, neighbor, stops + 1))
        return -1
