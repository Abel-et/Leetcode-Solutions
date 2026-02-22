class Solution:
    def binaryGap(self, n: int) -> int:
        # convet the give intger into binary
        binary = f'{n:b}'

        # cnt use to count the gap and maxc use to handle the maximum gap 
        cnt = 0
        max_gap = 0

        # catch if  current num is 1 and compare its gap from previous gaps and print max gap
        for end in range(len(binary)):
            if binary[end] == "1":
                cnt +=1

                # check the current count is greater than one else keep it unchanged
                if cnt > 1:
                    max_gap = max(cnt-1, max_gap)
                    cnt = 1
            else:
                cnt +=1
        
        return 0 if max_gap < 2 else  max_gap

            
