class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        st = ""
        for i in digits:
            st += str(i)
            
        digit = int(st) +1
        intoS = str(digit)

        arr = []
        for i in intoS:
            arr.append(int(i))
        return arr