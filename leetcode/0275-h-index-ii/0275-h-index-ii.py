class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        
        if n == 0:
            return 0
        
        left, right = -1, n
        
        while right - left > 1:
            mid = left + (right - left) // 2
            if citations[mid] == n - mid:
                return n - mid
            elif citations[mid] < n - mid:
                left = mid 
            else:
                right = mid 
          
        return n - right