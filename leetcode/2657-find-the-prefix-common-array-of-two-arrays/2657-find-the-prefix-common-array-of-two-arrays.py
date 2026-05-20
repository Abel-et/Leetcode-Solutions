class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a = set()
        b = set()

        common = 0
        c = []

        for i in range(len(A)):
            if A[i] != B[i]:
                a.add(A[i])
                b.add(B[i])
                p = len(a&b)
                c.append(p + common)
            else:
                common += 1
                c.append(len(a&b) + common)
        return c

