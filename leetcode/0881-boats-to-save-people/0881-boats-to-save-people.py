class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left,right= 0,len(people)-1
        cnt = 0
        # make sort the given peoples
        people.sort()

        if len(people) <2:
            return 1

        #checking the left and right part of the peoples weight  
        while left <= right :
            if people[left] + people[right] <= limit:
                cnt +=1
                left +=1
                right -=1
            else:
                right-=1
                cnt +=1
        return cnt

        