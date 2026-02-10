class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n= len(s)
        arr = []
        res = ""

        for i in range(n):
            arr.append([indices[i],s[i]])
        arr.sort(key = lambda x : x[0])
        for i in arr:
            res += i[1]
        return res