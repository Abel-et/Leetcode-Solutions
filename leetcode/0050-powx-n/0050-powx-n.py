class Solution:
    def myPow(self, x: float, n: int) -> float:
        # how it work is using binary multiplying insted of multiplying x n time 
        # just multiply xpow(2) and pow(n/2) times

        # this codition changes the x value into one over of x and back the n value into positive
        if n < 0:
            n = -n
            x = 1/x
        
        # this result will get value after multipling x on n is even value 
        # res = 1.0
        # while n > 0:
        #     if n%2 == 1:
        #         res*=x
        #     x *= x
        #     n = n//2
        # return res

        # using recursion
        # base case 
        if n == 0:
            return 1.0
        half = self.myPow(x,n//2)
        if n%2 == 0:
            return half* half
        if n%2 == 1:
            return half*half*x
        