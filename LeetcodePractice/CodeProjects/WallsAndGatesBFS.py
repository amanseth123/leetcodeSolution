You are given a m x n 2D grid initialized with these three possible values.

# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a Gate, that room should remain filled with INF
  # 2 Solutions scroll down for another 
from typing import (
    List,
)

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        
        ROWS,COLS = len(rooms),len(rooms[0])
        q=[]
        visit=set()
        def addRoom(newR,newC,dist):
            if newR<0 or newC<0 or newR==ROWS or newC==COLS or (newR,newC) in visit or rooms[newR][newC]==-1:
                return 
            visit.add((newR,newC))
            q.append((newR,newC,dist))
        for i in range(ROWS): # multi source BFS
            for j in range(COLS):
                if rooms[i][j]==0:
                    q.append((i,j,0))
                    visit.add((i,j))
        
        dist=0
        while q:
            for i in range(len(q)): #layerwise 
                r,c,dist = q.pop(0)
                rooms[r][c]=dist
                addRoom(r+1,c,dist+1)
                addRoom(r-1,c,dist+1)
                addRoom(r,c+1,dist+1)
                addRoom(r,c-1,dist+1)
                
                   
            #dist+=1
        return rooms
        # write your code here

        # OR
        #@nd Solution
        
from typing import (
    List,
)

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        
        ROWS,COLS = len(rooms),len(rooms[0])
        q=[]
        visit=set()
        # def addRoom(newR,newC):
        #     if newR<0 or newC<0 or newR==ROWS or newC==COLS or (newR,newC) in visit or rooms[newR][newC]==-1:
        #         return 
        #     visit.add((newR,newC))
        #     q.append((newR,newC))
        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j]==0:
                    q.append((i,j,0))
                    visit.add((i,j))
        
        dist=0
        while q:
            r,c,dist = q.pop(0)
            rooms[r][c]=dist
            for newR,newC in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0<=newR<ROWS and 0<=newC<COLS and (newR,newC) not in visit and rooms[newR][newC]!=-1:
                    visit.add((newR,newC))
                    q.append((newR,newC,dist+1))
            # for i in range(len(q)):
            #     r,c = q.pop(0)
            #     rooms[r][c]=dist
            #     addRoom(r+1,c)
            #     addRoom(r-1,c)
            #     addRoom(r,c+1)
            #     addRoom(r,c-1)   
            # dist+=1
        
        # write your code here


