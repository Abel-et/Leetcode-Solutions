class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # mapping the char form their last occured index 
        map = {c:i for i,c in enumerate(s)}

        # tools used to hold index, show the last first index
        result , start ,end = [],0,0

        for i , char in enumerate(s):
            end = max(end,map[char])

            # if the current char index equal to last index into map
            if i == end:
                result.append(i - start+1)
                start = i+1
        return result