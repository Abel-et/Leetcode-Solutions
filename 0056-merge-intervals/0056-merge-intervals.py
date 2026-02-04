class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        f=sorted(intervals, key = lambda x :x[1])
        s = sorted(f, key = lambda x :x[0])
        merged = []
        print(s)
        i =1
        n =len(s)
        if n ==1:
            return s
        
        for i in range(n-1):
            end = s[i][1]
            start = s[i+1][0]
            if start <= end:
                m=max(s[i+1][1],s[i][1])
                mm = min(s[i][0],s[i+1][0])
                merged.append([mm,m])
                print([mm,m])
            elif merged :
                m = len(merged)
                last = merged[m-1][1]
                print(s[i],"si")
                print(last,end)
                if last <end:
                    merged.append(s[i])
                else:
                    continue
            else:
                merged.append(s[i])
        
        p = len(merged)
        last = merged[p-1][1]
        il = s[n-1][1]
        if last < il:
            merged.append(s[n-1])
        return merged

