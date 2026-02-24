class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        cnt =0

        if len(citations) < 2:
            if citations[0] < 1:
                return 0
            else:
                return 1
        for i in range(len(citations)):
            if i+1 > citations[i]:
                return cnt
            else:
                cnt +=1
        else:
            return len(citations)
