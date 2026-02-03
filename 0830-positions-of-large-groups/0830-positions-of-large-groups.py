class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        count ,start = 0,0
        interval = []
        n = len(s)

        for i in range(n):
            if s[start] == s[i] :
                count +=1
                if i == n-1 and count >= 3 :
                    print('i am here')

                    interval.append([start,i])
                    return interval
            else:
                
                if count == 3 or count > 3:
                    interval.append([start,i-1])
                    
                    count = 0
                start = i
                count =1
                
        return interval