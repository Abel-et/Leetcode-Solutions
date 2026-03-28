class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
    
        # 1. Pre-validation: Diagonal must match remaining length
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""

        # 2. Greedy Construction
        res = [None] * n
        current_char_code = ord('a')
        for i in range(n):
            if res[i] is None:
                if current_char_code > ord('z'): return "" # Only 'a'-'z' allowed
                res[i] = chr(current_char_code)
                current_char_code += 1
            
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    res[j] = res[i]
                    
        s = "".join(res)

         # 3. Post-validation: Re-calculate LCP of 's' to verify full matrix
        actual_lcp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == s[j]:
                    if i == n - 1 or j == n - 1:
                        actual_lcp[i][j] = 1
                    else:
                        actual_lcp[i][j] = actual_lcp[i+1][j+1] + 1
                # If lcp[i][j] doesn't match the input, the matrix is invalid
                if actual_lcp[i][j] != lcp[i][j]:
                    return ""
                    
        return s