from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # hold the frequecey of word with there value
        freq = Counter(words)

        # creating buckets which is used to hold the word , at the bucket it belonge
        buckets = [[] for _ in range(len(words))]

        # helper fucntion which is used to sort the element which have same frequency to put lexicographically
        def insertion_sort(arr):

            for i in range(1,len(arr)):
                key  = arr[i]
                j = i-1

                while j >=0 and key < arr[j]:
                    arr[j+1] = arr[j]
                    j-=1
                arr[j+1] = key
            return arr

        for key , value in freq.items():
            buckets[value].append(key) #assign element to the bucket they belonge

        ans  = []
        
        for i in range(len(buckets)-1,-1,-1):
            if buckets[i]:
                sorted_bucket = insertion_sort(buckets[i])
                for element in sorted_bucket:
                    ans.append(element)
                    if len(ans) == k:
                        return ans