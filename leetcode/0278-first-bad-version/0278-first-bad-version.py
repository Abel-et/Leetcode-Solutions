# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        # the quesion have an isBadVersion fuction which reture the current version is bad or not  
        # our target is to minimize calling the  this function 
        #  so we  use binary search becuse it's time complexity is O(logn) and the 
        #  the question is sorted which means it start from 1 , n  thing .
        left = 0
        right = n

        while left < right:
            mid = (left + right)//2
            # check the mid is bad or not  update the right if it is bad only
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left