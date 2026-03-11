class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_nums = deque()
        min_nums = deque()
        left = 0

        max_size = 0

        for i in range(len(nums)):

            # putting min number in min_nums deque whichi is the curr nums is less than in deque
            while min_nums and min_nums[-1] > nums[i]:
                min_nums.pop()
            min_nums.append(nums[i])

            # putting curr max num in max deque which is the curr nums is greather than last deque
            while max_nums and max_nums[-1] < nums[i]:
                max_nums.pop()
            max_nums.append(nums[i])

            # if the condition is invalid means the max and min deque  differences is greater than limit
            # in another way if the max value of the window and min value of the window greater the limit val
            while max_nums[0] - min_nums[0] >limit:

                # shrinking the window until , the max and min value of window less than limit val
                if max_nums[0] == nums[left]:
                    max_nums.popleft()
                if min_nums[0] == nums[left]:
                    min_nums.popleft()
                left +=1
            
            # getting the max size of subarray 
            max_size = max(max_size, i - left + 1)
            
        return max_size