class Solution:
    def FirstNonRepeating(self, A):
       freq=[0]*26
       q=[]
       ans=''
       for i in range(len(A)):
           c = A[i]
           freq[ord(c)-97]+=1
           if freq[ord(c)-97]==1:
               q.append(c)
           else:
               while q and freq[ord(q[0])-97]>1:
                   q.pop(0)
           if q:
               ans+=q[0]
           else:
               ans+='#'
       return ans
   def FirstNonRepeating2(self, A):
       uniqueList = []
       repeatedList = []
       sol = ""
            
       for i, c in enumerate(A):
           try: #if c in uniqueList
               uniqueList.remove(c)
               repeatedList.append(c)
           except:
               if c not in repeatedList:
                   uniqueList.append(c)
               
           if uniqueList:
               sol+=uniqueList[0]
           else:
               sol+='#'
           
       return sol