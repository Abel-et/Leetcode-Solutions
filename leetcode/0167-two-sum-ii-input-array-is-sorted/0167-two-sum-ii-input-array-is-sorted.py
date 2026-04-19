class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left , right = 0 ,len(numbers)-1
        
        #  using colliding pointer approach 
        while left < right:
            if (numbers[left] + numbers[right]) == target:
                return [left + 1 , right + 1]
            elif (numbers[left] + numbers[right])  > target:
                right -=1
            else:
                left +=1 
