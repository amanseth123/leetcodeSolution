from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.next={}
        self.isWord=False
        
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr=self.head
        for ch in word :
            if ch not in curr.next:
                curr.next[ch]=TrieNode()
            curr=curr.next[ch]
        curr.isWord=True

    def search2(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(index,root):
            curr=root
            if index==len(word):
                return curr.isWord
            for i in range(index,len(word)):
                if word[i]=='.':
                    return any(dfs(i+1,node) for node in curr.next.values())
                else:
                    if word[i] in curr.next:
                        curr=curr.next[word[i]]
                        #dfs(i+1,curr)
                    else:
                        return False
            return curr.isWord
        return dfs(0,self.head)

    
    
                # 2nd SOLUTION

from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.next=defaultdict(TrieNode)
        self.isWord=False
        
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=TrieNode()
        
        
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr=self.head
        for ch in word :
            curr=curr.next[ch]
        curr.isWord=True
        
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def helper(i,curr):
            if i==len(word):
                return curr.isWord
            if word[i]=='.':
                return any(helper(i+1,next_node) for next_node in curr.next.values())
            if word[i] not in curr.next:
                return False
            return helper(i+1,curr.next[word[i]])
                
        
        return helper(0,self.head)
        
        
        
        
        
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)