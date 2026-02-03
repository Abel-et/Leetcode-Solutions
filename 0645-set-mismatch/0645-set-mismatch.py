class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n= len(nums)
        unque = set(nums)
        # Duplicated num
        dup =0
        for i in unque:
            if nums.count(i)>1:
                dup = i
                nums.remove(i)
                break
        print(nums)

         # missing value
         
        missing = 0
        nums.sort()
        for index,value in enumerate(nums):
            if index+1 != value:
                missing = index+1
                break   
        else:
            missing = max(unque) + 1
        return [dup ,missing]

        
       
       