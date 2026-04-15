class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0
        
        def divide(left, right):
            if left >= right:
                return [nums[left]] if left == right else []
            
            mid = left + (right - left) // 2
            left_part = divide(left, mid)
            right_part = divide(mid + 1, right)
            
            # --- COUNT STEP ---
            # Count pairs where left_part[i] > 2 * right_part[j]
            j = 0
            for i in range(len(left_part)):
                while j < len(right_part) and left_part[i] > 2 * right_part[j]:
                    j += 1
                self.count += j
            
            # --- MERGE STEP ---
            return combine(left_part, right_part)

        def combine(left, right):
            result = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result

        if not nums: return 0
        divide(0, len(nums) - 1)
        return self.count
