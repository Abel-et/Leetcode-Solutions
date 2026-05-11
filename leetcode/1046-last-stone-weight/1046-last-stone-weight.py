import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap_max = [-x for x in stones]
        heapq.heapify(heap_max)
        n = len(stones)
        print(heap_max)

        if n < 2:
            return stones[0]
        for i in range(n):
            if len(heap_max) > 1:
                y = - heapq.heappop(heap_max)
                x = - heapq.heappop(heap_max)
                print(y, x)
                if x == y:
                    n -= 2
                else:
                    heapq.heappush(heap_max , -(y - x))
                    n = -1
                print(heap_max)
            else:
                return -heap_max[0] if heap_max else 0
    

        
      
       
