from collections import defaultdict

class Solution:
    def distance(self, nums: list[int]) -> list[int]:
        n = len(nums)
        groups = defaultdict(list)
        ans = [0] * n

        # Group indices by their value
        for i, val in enumerate(nums):
            groups[val].append(i)

        # For each group, calculate distances using prefix sums
        for val in groups:
            indices = groups[val]
            m = len(indices)
            
            # Calculate initial distance for the first element in the group
            current_dist = sum(indices) - (m * indices[0])
            ans[indices[0]] = current_dist
            
            # Use the previous result to calculate the next in O(1)
            # Formula: dist_i = dist_{i-1} + (2*i - m) * (indices[i] - indices[i-1])
            for j in range(1, m):
                delta = indices[j] - indices[j-1]
                current_dist += (2 * j - m) * delta
                ans[indices[j]] = current_dist
                
        return ans
