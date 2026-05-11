class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []

        for i in nums:
            if i > 9:
                for d in str(i):
                    answer.append(int(d))
            else:
                answer.append(i)
        return answer