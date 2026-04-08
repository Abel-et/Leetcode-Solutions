from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique = Counter(nums)

        # create a bucktes with the length of arr to hold the  frequnce based on its index
        # buckets = [[] for _ in range(len(nums)+1)]

        # for key , value in  unique.items():
        #     buckets[value].append(key) #assigne each element based on there frequence at index of bucket

        # answer = []

        # for i in range(len(buckets)-1,-1,-1):
        #     for ele in buckets[i]:
        #         answer.append(ele)
        #         if len(answer) == k:
        #             return answer

        arr = []
        for _ in range(k):
            max_element = max(unique,key= unique.get)
            arr.append(max_element)
            if unique:
                unique.pop(max_element)
        return arr

       