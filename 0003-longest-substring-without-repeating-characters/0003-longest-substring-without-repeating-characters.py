class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # creating a set , two pointers, and counter t
        sub = set()
        left ,right = 0,0
        n = len(s)
        maxC =0

        # if there is a single element in that set return one 
        if len(set(s))==1:
            return 1

        # if s has no any element
        if not s :
            return 0

        # checking every elemnets of s and if the current element is in 
        # the set catch the previous length and  update the left pointer 
        while right < n:
            print(sub,s[left:right])
            if s[right] in sub:
                maxC = max(len(sub),maxC)
                
                # check the current char in the set  and left pointer less than the right remove the char of 
                # left 
                while s[right] in sub and left < right :
                    sub.discard(s[left])
                    left +=1
                sub.add(s[right])
            else:
                sub.add(s[right])
                
            right +=1 
        return max(maxC,len(sub))
            


              

