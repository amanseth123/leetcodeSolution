def dfs(node): 
    if node in exploring:
        return exploring[node]
    if node in explored:
        return True
    exploring[node]=False
    for child in graph[node]:
        if dfs(child)==False:
            return False
    exploring[node]=True
    explored.add(node)
    ans.append(node)
    return True
def dfs2(node):
    if node in visited:
        return visited[node]
    visited[node] =False
    for q in graph[node]:
        if dfs2(q)==False:
            return False
    visited[node]=True
    
graph=defaultdict(list)
for i,j in prerequisites:
    graph[i].append(j)
#print(in_degree,graph)
exploring={}
explored=set()
visited={} #used only for dfs2 
ans=[]
for node in range(numCourses):
    if dfs(node)==False:
        print([])
# for i in q:
#     if i not in visited:
#         ans.append(i)
print(ans)
