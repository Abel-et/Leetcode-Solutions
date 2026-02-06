class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        arr = []
        
        for i in nums:
            if i in hash:
                hash[i] +=1
            else:
                hash[i] = 1
        
        for i in range(k):
            maxValue = max(hash , key= hash.get)
            arr.append(maxValue)
            if hash:
                hash.pop(maxValue)
        return arr