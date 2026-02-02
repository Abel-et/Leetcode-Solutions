class Solution(object):
    def scoreBalance(self, s):
        """
        :type s: str
        :rtype: bool
        """
        value =[]
        for i in s:
            
            value.append(ord(i)-96)
        print(value)
        total = sum(value)
        left =0
        for i in range(len(value)):
            left += value[i]
            remain = total - left
            if remain < 0:
                return False
            elif left == remain:
                return True
        else:
            return False