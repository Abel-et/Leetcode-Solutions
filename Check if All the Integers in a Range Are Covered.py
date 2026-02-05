class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        n = len(ranges)
        arr = set()
        for i in range(n):
            start = ranges[i][0]
            end = ranges[i][1]
            for j in range(start,end+1):
                arr.add(j)

        for i in range(left, right+1):
            if i not in arr:
                return False
        else:
            return True
