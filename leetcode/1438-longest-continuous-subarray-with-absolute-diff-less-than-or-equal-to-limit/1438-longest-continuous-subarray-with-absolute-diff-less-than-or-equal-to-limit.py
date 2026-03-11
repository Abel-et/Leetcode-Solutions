class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_nums = deque()
        min_nums = deque()
        left = 0

        max_size = 0

        for i in range(len(nums)):

            # putting min number in min_nums deque

            while min_nums and min_nums[-1] > nums[i]:
                min_nums.pop()
            min_nums.append(nums[i])

            while max_nums and max_nums[-1] < nums[i]:
                max_nums.pop()
            max_nums.append(nums[i])

            # if the condition is invalid
            while max_nums[0] - min_nums[0] >limit:
                if max_nums[0] == nums[left]:
                    max_nums.popleft()
                if min_nums[0] == nums[left]:
                    min_nums.popleft()
                left +=1
            max_size = max(max_size, i - left + 1)
        return max_size