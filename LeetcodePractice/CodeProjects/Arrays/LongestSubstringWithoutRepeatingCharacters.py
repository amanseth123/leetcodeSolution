class Solution:
    def lengthOfLongestSubstring2(self, s: str) -> int:
        if len(s)==0:
            return 0
        '''
        if len(s)==1:
            return 1
        lo,hi=0,0
        di={}
        m=0
        while lo<=hi and hi<len(s):
            if s[hi] not in di:
                di[s[hi]]=1
                m=max(m,hi-lo+1)
                hi+=1
            else:
                del di[s[lo]]
                lo+=1
        return m
        '''
        di={}
        m=0 
        start=0
        for i in range(len(s)):
            if s[i] in di and start<=di[s[i]]: 
                #why start<=di[s[i]] consider the case "tmmzuxt" at i==6 t gets repeated and to make sure that the start point to index after 1st m we need to fo start<=di[s[i]]
                start=di[s[i]]+1
            else: #consider case "dvdf" we have to update m even if no duplicates occur and ans is 3
                m=max(m,i-start+1)
                
            di[s[i]]=i
        #print(di)
        return m
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        st = set()
        res = 0
        left = 0
        for right in range(len(s)):
            while s[right] in st: # squeeeze from left because we want subarrays
                st.remove(s[left])
                left+=1 #increment the left because we're not considering s[left]
            st.add(s[right])
            res = max(res,right-left+1)
        return res

# two methods-> one either jump out of the hurdle or eliminate all previous ladder to reach the answer

