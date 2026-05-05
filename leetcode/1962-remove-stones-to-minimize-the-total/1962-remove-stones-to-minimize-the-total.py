from heapq import  heapify, heappop , heappush
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] = - piles[i]
        heapify(piles)
        print(piles)

        for _ in range(k):
            temp = heappop(piles)
            temp = -temp
            temp = ceil(temp/2)

            heappush(piles, -temp)
        return - sum(piles)

            
        