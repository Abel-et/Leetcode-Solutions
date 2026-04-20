import math 
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # two poitner form staring and square of c  
        left , right = 0, int(c**0.5)
        while left <= right:
            total = left * left + right * right
            
            if total == c:
                return True
            elif total < c:
                left +=1
            else:
                right -=1
        return False
