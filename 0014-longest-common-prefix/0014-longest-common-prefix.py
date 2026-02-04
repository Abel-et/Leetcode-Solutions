class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out=""
        x=min(strs)
        for i in range(len(x)):
            y=x[i]
            for j in  range(len(strs)):
                if y!=strs[j][i]:
                    return out
            out+=x[i]
        return out