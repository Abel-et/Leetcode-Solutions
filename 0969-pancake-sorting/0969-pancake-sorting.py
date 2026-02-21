class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)

        for curr in range(n, 1, -1):
            idx = arr.index(curr)

            # already in correct position
            if idx == curr - 1:
                continue

            # move curr to front if not already there
            if idx != 0:
                res.append(idx + 1)
                arr[:idx + 1] = reversed(arr[:idx + 1])

            # move curr to its correct position
            res.append(curr)
            arr[:curr] = reversed(arr[:curr])

        return res