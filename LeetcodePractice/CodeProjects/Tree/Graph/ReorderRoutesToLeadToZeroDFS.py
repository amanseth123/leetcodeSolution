class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(a,b) for a,b in connections}
        
        neighbours = {city:[] for city in range(n)}
        changes = 0
        visit=set()
        for a,b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)
        def dfs(node):
            nonlocal edges, changes, neighbours, visit
            for neig in neighbours[node]:
                if neig in visit:
                    continue
                if (neig,node) not in edges:
                    changes+=1
                visit.add(neig)
                dfs(neig)
        visit.add(0)
        dfs(0)
        return changes
        
        
        
        
        