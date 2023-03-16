

class Solution:
    # BFS Solution
    def findItinerary2(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        stack=['JFK']
        di=defaultdict(list)
        for i,j in tickets:
            di[i].append(j)
        print(di)
        ans=[]
        while stack:
            answer=stack[-1] # we need to fill stack with all the neighbour values because its possible that the only child we pop doesn't have any neighbour and we'll be stuck at that point
            if di[answer]:
                #print(di[answer])
                stack.append(di[answer].pop())
                continue
            #print(stack,"stack")
            ans.append(stack.pop())
        return reversed(ans)
    
    
    #   DFS Solution
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj={src:[] for src,dst in tickets}
        for i,j in tickets:
            adj[i].append(j)
        #print(adj) #{'ATL': ['JFK', 'SFO'], 'JFK': ['ATL', 'SFO'], 'SFO': ['ATL']}
        #edge case [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]

        res=["JFK"]
        def dfs(src):
            if len(res) == len(tickets)+1:
                return True
            if src not in adj:
                return False
            temp = list(adj[src])
            for i,v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                adj[src].insert(i,v) #backtrack
                res.pop()
            return False
        dfs("JFK")
        return res #O((V+E)^2 or if E==V then V^2 , space complexity O(E))
        
        
        
        
        
        
        
        
        
        
        

