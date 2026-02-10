class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []

        for i in nums:
            if i <10:
                answer.append(i)
            else:
                k = str(i)
                for i in k:
                    answer.append(int(i))
        return answer