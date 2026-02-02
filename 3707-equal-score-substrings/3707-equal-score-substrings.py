class Solution(object):
    def scoreBalance(self, s):
        """
        :type s: str
        :rtype: bool
        """
        value =[]
        total = 0
        for i in s:
            index = ord(i)-96
            value.append(index)
            total += index
        print(value)


       
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