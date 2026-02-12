from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        #  the problem is saying that sort the given elements by their frequcny decsending order

        # creating counter which help as to hold the chars with ther freq and ans  string for returning answer
        container = Counter(s)
        ans = ''
        
        # sorting the give counter based on its values decreasing order 
        sorted_by_freq = sorted(container.items(), key = lambda x: x[1] ,reverse = True)
       
    #    travers through all sorted elements and construct  ans string
        for i in sorted_by_freq:
            char = i[0]
            freq = i[1]
            for _ in range(freq):
                ans += char
        
        return ans

        
        