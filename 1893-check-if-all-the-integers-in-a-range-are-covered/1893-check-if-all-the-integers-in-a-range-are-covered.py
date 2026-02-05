class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        n = len(ranges)
        ranges.sort(key = lambda x: x[0])
        print(ranges)
        for i in range(n):
            start = ranges[i][0]
            end = ranges[i][1]
            if start <= left and end>= left:
                print('i here ',start,end)
                if start <= right and right <= end:
                    return True
                else:
                    j = i+1
                    while j < n:
                        s = ranges[j][0]
                        e = ranges[j][1]

                        ps = ranges[j-1][0] +1
                        pe = ranges[j-1][1] + 1
                        print('in while loop',s,e , ps, pe)
                        if (ps == s or ps == e) or (pe == s or pe == e):

                            if s >= right or e >= right:
                                return True
                        j+=1
        else:
            return False