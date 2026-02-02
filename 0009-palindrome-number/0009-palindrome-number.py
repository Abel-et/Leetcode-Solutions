class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        palindrome = str(x)
        if(palindrome == palindrome[::-1]):
            return True
        return False
        