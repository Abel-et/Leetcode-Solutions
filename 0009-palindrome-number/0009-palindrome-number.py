class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # palindrome = str(x)
        # if(palindrome == palindrome[::-1]):
        #     return True
        # return False

        if x < 10 and x >= 0 :
            return True
        if x < 0 or x%10 == 0 :
            return False
        half = 0
        while x > half:
            half = half*10 +x%10
            x//=10
        return x == half or x == half//10

        