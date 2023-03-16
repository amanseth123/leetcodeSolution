from typing import (
    List,
)

class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        self.count=0
        par=[x for x in range(len(edges)+1)]
        rank = [1 for _ in range(len(edges)+1)]
        di={}
        def find(tp):
            p=par[tp]
            while p!=par[p]:
                par[p]=par[par[p]]
                p=par[p]
            return p
        def union(p1,p2):
            x,y = find(p1),find(p2)
            if x in di:
                di[x]+=1
            else:
                di[x]=1
            if y in di:
                di[y]+=1
            else:
                di[y]=1
            if x==y:
                return False
            if rank[x]>rank[y]:
                par[y]=x
                rank[x]+=rank[y]
            else:
                par[x]=y
                rank[y]+=rank[x]
            return True
        if n==1 and edges==[]:
            return True
        if n>1 and edges==[]:
            return False
        for p1,p2 in edges:
            if union(p1,p2)==False:
                return False
        print(di)
        return True and len(di)==n
        # write your code here
    
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if n==0:
            return True
        adj = {i:[] for i in range(n)}
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        visit=set()
        def dfs(i,parent):
            if i in visit:
                return False
            visit.add(i)
            for j in adj[i]:
                if j==parent:
                    continue
                if not dfs(j,i):
                    return False
            return True
     
        return dfs(0,-1) and n==len(visit)




        # write your code here
