class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)

        for l, r, d in shifts:
            val = 1 if d == 1 else -1
            diff[l] += val
            diff[r + 1] -= val

        res = []
        cur = 0

        for i in range(n):
            cur += diff[i]

            # convert char to number
            x = ord(s[i]) - ord('a')

            # apply shift
            x = (x + cur) % 26

            res.append(chr(x + ord('a')))

        return "".join(res)