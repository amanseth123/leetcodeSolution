from collections import defaultdict



#Leetcode course schedule 207

def hasCycle(node):
    if node in visited:
        return visited[node]
    visited[node]=True # in exploring and found again 
    for i in graph[node]:
        if hasCycle(i):
            return True
    visited[node] = False

visited={} # or visited=set()  # False=visited True=current Path not completely visited
graph=defaultdict(list)
