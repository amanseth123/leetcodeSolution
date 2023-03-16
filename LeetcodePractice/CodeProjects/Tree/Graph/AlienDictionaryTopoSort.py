from heapq import *
class Solution:
    def alienOrder2(self, words):
        adj = {c:set() for w in words for c in w}
        for i in range(len(words)-1):
            w1,w2=words[i],words[i+1]
            minLen = min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:minLen]==w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visit={} # False=visited True=current Path not completely visited
        res=[]
        def dfs(c):
            if c in visit:
                return visit[c] # in exploring and found again 
            visit[c]=True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c]=False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""
        return "".join(res[::-1])
    def alienOrder(self, words):
        # Construct Graph
        in_degree = {ch: 0 for word in words for ch in word}
        neighbors = {ch: [] for word in words for ch in word}
        for pos in range(len(words) - 1):
            for i in range(min(len(words[pos]), len(words[pos+1]))):
                pre, next = words[pos][i], words[pos+1][i]
                if pre != next:
                	in_degree[next] += 1
                    neighbors[pre].append(next)
                    break
        
        # Topological Sort
        heap = [ch for ch in in_degree if in_degree[ch] == 0]
        heapify(heap)
        order = []
        while heap:
            for _ in range(len(heap)):
                ch = heappop(heap)
                order.append(ch)
                for child in neighbors[ch]:
                    in_degree[child] -= 1
                    if in_degree[child] == 0:
                        heappush(heap, child)
        
        # order is invalid
        if len(order) != len(in_degree):
            return ""
        return ''.join(order)