class Solution:
    def isHappy2(self, n: int) -> bool:
        n_str = list(str(n))
        visit=set()
        while True:
            new = 0
            for i in n_str:
                new+=(int(i)**2)
            n_str = str(new)
            if n_str in visit:
                return False
            visit.add(n_str)
            if n_str=="1":
                return True
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(n):
            output = 0
            while n:
                digit = n%10
                digit = digit**2
                output+=digit
                n=n//10
            return output
        n_str = list(str(n))
        visit=set()
        while True:
            n = sumOfSquares(n)
            if n in visit:
                return False
            visit.add(n)
            if n==1:
                return True