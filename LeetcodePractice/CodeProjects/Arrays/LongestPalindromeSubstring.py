class Solution:
    def longestPalindrome(self,s:str)->str:
        n=len(s)
        self.res=""
        maxLen = 0
        for i in range(n): # iterating through each element considering them as center of the string and expanding outwards
            
            l,r = i,i #odd length
            while l>=0 and r<n and s[l]==s[r]:
                #print("tst")
                if r-l+1>maxLen:
                    self.res = s[l:r+1]
                    maxLen = r-l+1
                    #print("Update",self.res,maxLen,l,r)
                l-=1
                r+=1
            l,r = i,i+1 # even lenght
            while l>=0 and r<n and s[l]==s[r]:
                #print("check")
                if r-l+1>maxLen:
                    self.res = s[l:r+1]
                    maxLen = r-l+1
                    #print("Update2",self.res,maxLen,l,r)
                l-=1
                r+=1
        return self.res
    def longestPalindrome2(self, s: str) -> str:    
        # this won't work for case "ac" where the answer is "a" but this code will give "" because the length is even but the answer is referenced from odd length
        n=len(s)
        self.res=""
        maxLen = 0
        if n%2!=0:
            for i in range(n):
                l,r = i,i
                while l>=0 and r<n and s[l]==s[r]:
                    #print("tst")
                    if r-l+1>maxLen:
                        self.res = s[l:r+1]
                        maxLen = r-l+1
                        #print("Update",self.res,maxLen,l,r)
                    l-=1
                    r+=1
        else:
            for i in range(n):
                l,r = i,i+1
                print(s,l,r)
                while l>=0 and r<n and s[l]==s[r]:
                    #print("check")
                    if r-l+1>maxLen:
                        self.res = s[l:r+1]
                        maxLen = r-l+1
                        #print("Update2",self.res,maxLen,l,r)
                    l-=1
                    r+=1
        return self.res
        
        
        