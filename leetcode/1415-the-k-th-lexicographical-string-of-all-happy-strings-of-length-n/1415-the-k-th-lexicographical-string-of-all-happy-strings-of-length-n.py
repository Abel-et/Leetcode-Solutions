class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # Total happy strings possible
        total = 3 * (2**(n - 1))
        
        if k > total:
            return ""
        
        # Define choices and initial state
        choices = ['a', 'b', 'c']
        res = []
        
        # Adjust k to 0-indexed for easier math
        k -= 1
        
        # Determine the first character
        # Each starting char ('a', 'b', 'c') has 2^(n-1) strings
        partition_size = 2**(n - 1)
        index = k // partition_size
        res.append(choices[index])
        
        # Determine the remaining n-1 characters
        k %= partition_size
        for i in range(n - 1):
            partition_size //= 2
            # Remaining choices are the two letters NOT used in the previous step
            options = [c for c in choices if c != res[-1]]
            
            index = k // partition_size
            res.append(options[index])
            k %= partition_size
            
        return "".join(res)