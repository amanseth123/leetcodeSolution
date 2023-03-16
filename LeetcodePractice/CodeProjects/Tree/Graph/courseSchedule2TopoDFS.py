'''
from collections import defaultdict
class Solution:
    # we cannot use normal topological sort because we have to take care of cycle as well
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        in_degree=defaultdict(int)
        for i,j in prerequisites:
            graph[i].append(j)
            in_degree[j]+=1
        q=[nodes for nodes in range(numCourses) if nodes not in in_degree]
        ans=[]
        count=0
        while q:
            temp=q.pop(0)
            ans.append(temp)
            count+=1
            for child in graph[temp]:
                in_degree[child]-=1
                if in_degree[child]==0:
                    q.append(child)
        if count==numCourses:
            return ans[::-1]
        return []        

from collections import defaultdict
class Solution:
    # we cannot use normal topological sort because we have to take care of cycle as well
    def findOrder(self, numCourses, prerequisites):
        graph=defaultdict(list)
        in_degree=defaultdict(int)
        for i,j in prerequisites:
            graph[i].append(j)
            in_degree[j]+=1
        q=[i for i in range(numCourses) if i not in in_degree]
        ans=[]
        while q:
            temp=q.pop(0)
            ans.append(temp)
            for child in graph[temp]:
                in_degree[child]-=1
                if in_degree[child]==0:
                    q.append(child)
        if len(ans)==numCourses:
            return ans[::-1]
        return []
        
        def dfs(node,explored,exploring,ans):
            exploring.add(node)
            if node in graph:
                for child in graph[node]:
                    if child in explored:
                        continue
                    if child is exploring:
                        return False
                    if not dfs(child,explored,exploring,ans):
                        return False
            exploring.remove(node)
            explored.add(node)
            ans.append(node)
            return True
        graph=defaultdict(list)
        for edge in prerequisites:
            if edge[0] in graph:
                graph[edge[0]].append(edge[1])
            else:
                graph[edge[0]] = [edge[1]]
        
        exploring=set()
        explored=set()
        ans=[]
        for node in range(numCourses):
            if node in explored:
                continue
            if not dfs(node,explored,exploring,ans):
                return []
        return ans
'''
class Solution:
    # we cannot use normal topological sort because we have to take care of cycle as well
    def findOrder(self, numCourses, prerequisites):
        '''
        graph=defaultdict(list)
        in_degree=defaultdict(int)
        for i,j in prerequisites:
            graph[i].append(j)
            in_degree[j]+=1
        q=[i for i in range(numCourses) if i not in in_degree]
        ans=[]
        while q:
            temp=q.pop(0)
            ans.append(temp)
            for child in graph[temp]:
                in_degree[child]-=1
                if in_degree[child]==0:
                    q.append(child)
        if len(ans)==numCourses:
            return ans[::-1]
        return []
        '''
        #dfs approach
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
            ans.append(node) #post order traversal
            return True
        def dfs2(node):
            if node in visited:
                return visited[node]
            visited[node] =False
            for q in graph[node]:
                if dfs2(q)==False:
                    return False
            visited[node]=True
            ans.append(node) #postorder traversal
            
        graph=defaultdict(list)
        for i,j in prerequisites:
            graph[i].append(j)
        #print(in_degree,graph)
        exploring={} #we can have this as set too instead of having it as a dictionary
        explored=set()
        ans=[]
        visited={} #used only for dfs2
        for node in range(numCourses):
            if dfs2(node)==False:
                return []
        # for i in q:
        #     if i not in visited:
        #         ans.append(i)
        return ans