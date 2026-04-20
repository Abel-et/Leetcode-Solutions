class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        if n < 2:
            return 1

        # make sort the give peoples by ther weight 
        people.sort()

        # required boat
        boat = 0  


        # using colliding two pointer apperoach 
        left , right = 0 , n - 1

        while left <= right:

            # if the largest wight is equal to the limit or the sum of minimun wight and largest wight 
            # greater than than the limit update the right pointer and increate the boat by one
            if people[right] == limit or (people[left] + people[right])> limit:
                boat += 1
            
            else:
                left , boat = left + 1 , boat +1 
            right -= 1

        return boat

        