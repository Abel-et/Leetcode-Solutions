class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort(key = lambda x :x[0])
        m = [intervals[0]]

        for i in range(1,len(intervals)):
            start = intervals[i][0]
            end = m[-1][1]

            if start <= end:
                m[-1][1]= max(intervals[i][1],end)
            else:
                m.append(intervals[i])
        return m
                

        