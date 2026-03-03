class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"

        for i in range(n-1):
            revers = list(s)
            revers.reverse()
            for j in range(len(revers)):
                if revers[j] == '0':
                    revers[j] = '1'
                else:
                    revers[j] = "0"
            s += '1' + "".join(revers)
        return s[k-1] if k <= len(s) else None
