'''
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
'''



class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node
        #left=LRU, right=most recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left #initially connect them together 

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    # insert node at right, just before the right pointer
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            print(lru in self.cache)
            del self.cache[lru.key]



from collections import defaultdict 
class LRUCache2:
    def __init__(self, capacity: int):
        self.di={}
        self.capacity=capacity
    def get(self, key: int) -> int:
        if key in self.di:
            value=self.di[key]
            self.di.pop(key)
            self.di[key]=value
            return value
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.di:
            v=self.di.pop(key)
            self.di[key]=v
        elif len(self.di)==self.capacity:
            self.di.pop(list(self.di.keys())[0])
        self.di[key]=value
        '''
        if key in self.di:
            self.di.pop(key)
        elif len(self.di)==self.capacity:
            self.di.pop(list(self.di.keys())[0])
        self.di[key]=value'''
        
        
        
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)











