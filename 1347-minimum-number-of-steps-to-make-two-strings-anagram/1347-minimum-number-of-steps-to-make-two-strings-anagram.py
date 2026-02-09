from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sCounter = Counter(s)
        tCounter = Counter(t)
        count_step = 0

        for key,value in tCounter.items():
            if key not in sCounter :
                count_step +=value
            elif sCounter[key] < value:
                count_step += value - sCounter[key]
        return count_step
        