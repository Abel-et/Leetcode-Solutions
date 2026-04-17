class Solution:
    def minMirrorPairDistance(self, nums: list[int]) -> int:
        
        def get_reverse(n: int) -> int:
            # Reverses digits and handles leading zeros automatically
            return int(str(n)[::-1])

        # Maps the required mirror value -> the index where its reverse was seen
        # e.g., if we see 12 at index 0, we store {21: 0}
        targets = {}
        min_dist = float('inf')
        found = False

        for j in range(len(nums)):
            current_val = nums[j]
            
            # 1. Check if the current number completes a mirror pair
            if current_val in targets:
                found = True
                distance = j - targets[current_val]
                if distance < min_dist:
                    min_dist = distance
            
            # 2. Add the reverse of the current number to our search dictionary
            # We always update to the latest index to keep the distance minimal
            rev_val = get_reverse(current_val)
            targets[rev_val] = j

        return min_dist if found else -1
