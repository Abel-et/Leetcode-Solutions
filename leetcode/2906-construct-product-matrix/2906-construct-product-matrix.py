class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        arr = []
        mod = 12345

        for row in grid:
            arr.extend(row)

        size = len(arr)
        prefix = [1]*size

        for i in range(1,size):
            prefix[i] = (prefix[i-1]*arr[i-1]) % mod
        
        suffix = [1]*size
        for i in range(size-2,-1,-1):
            suffix[i] = (suffix[i+1]*arr[i+1])% mod
        
        idx = 0
        res = []
        for i in range(len(grid)):
            row = []
            for j in range(len(grid[0])):
                row.append((suffix[idx]*prefix[idx])% mod)
                idx += 1
            res.append(row)
        return res