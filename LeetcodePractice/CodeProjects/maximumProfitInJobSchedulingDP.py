class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        start=startTime
        end=endTime
        n = len(start)
        start, end, profit = zip(*sorted(zip(start, end, profit)))
        jump = {i: bisect.bisect_left(start, end[i]) for i in range(n)} #if we consider to start the job at ith start time then we need to consider the profit at end time and for that we need dp[good place for end time such that other task can also start after it]
        dp = [0 for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            
            dp[i] = max(dp[i+1], profit[i] + dp[jump[i]])
        return dp[0]