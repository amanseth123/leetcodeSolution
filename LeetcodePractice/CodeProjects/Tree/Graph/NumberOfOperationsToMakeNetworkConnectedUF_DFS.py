class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        #valid for both scenarios 
        


        # if we have N connected components then the number of edges we need to make all nodes connected is N-1
        # minimum number of edges needed to connect a graph of n nodes is n-1
        
        
        # Using simple dfs(ACCEPTED)
        # if len(connections)<n-1:
        #     return -1
        # visit=set()
        # graph = defaultdict(list)
        # def dfs(node):
        #     if node in visit:
        #         return 
        #     visit.add(node)
        #     for nei in graph[node]:
        #         dfs(nei)
        # for i,j in connections:
        #     graph[i].append(j)
        #     graph[j].append(i)
        # count=0
        # for i in range(n):
        #     if i not in visit:
        #         dfs(i)
        #         count+=1
        # return count-1
        
        #Using union find
        if len(connections)<n-1:
            return -1
        par = [i for i in range(n)]
        rank = [1]*n
        def find(n1):
            res=n1
            while n1!=par[n1]:
                par[res],res=par[par[res]],par[res]
            return res
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1==p2:
                return 0
            if rank[p2]>rank[p1]: #p1 will be the child of p2 i.e p2 will be the new parent 
                par[p1]=p2 # p2 is gonna be the parent of p1
                rank[p2]+=rank[p1] #updating that accordingly
            else: 
                par[p2]=p1
                rank[p1]+=rank[p2]
            return 1
        res=n
        for n1,n2 in connections:
            res-=union(n1,n2) #connected components will be len(set(rank)) but for it make rank global or otherwise return 1 when there's a connected component returned from union
            # function and subtract it from n because number of connected components can't exceed n(number of nodes)
        return res-1 #res=number of connected components but res-1 will give min edges needed to connect them
                
        
        
        
        
        
        
        
        