class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if not s or len(s) == 0:
            return ""
        
        # Track the start and length of the longest palindrome found
        start = 0
        max_len = 0
        
        def expand(left, right) :
            # Expand as long as pointers are in bounds and characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return length of palindrome found: (right - 1) - (left + 1) + 1
            return right - left - 1

        for i in range(len(s)):
            # Case 1: Odd length (center is a single character like "aba")
            len1 = expand(i, i)
            # Case 2: Even length (center is between two characters like "abba")
            len2 = expand(i, i + 1)
            
            current_max = max(len1, len2)
            if current_max > max_len:
                max_len = current_max
                # Calculate new starting index based on center and length
                start = i - (current_max - 1) // 2
                
        return s[start : start + max_len]
