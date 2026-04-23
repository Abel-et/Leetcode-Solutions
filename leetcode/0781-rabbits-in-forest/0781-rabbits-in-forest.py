from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbits = Counter(answers)
        result = 0

        for ans , freq in rabbits.items():
            expected = ans + 1
            if ans == 0:
                result += freq
                continue
            if freq > expected:
                prod = (freq// expected)* expected if freq % expected != 0 else (freq // expected)
                result += expected + prod

            else:
                result += expected
        return result

