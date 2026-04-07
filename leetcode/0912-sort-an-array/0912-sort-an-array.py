class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        
        # divide every element in the arry until it reach base case
        def Divide(left, right, arr):
            if left == right:
                return [arr[left]]
            
            mid = left + (right-left)//2
            left_half = Divide(left , mid, arr)
            right_half = Divide(mid+1, right, arr)

            return combine(left_half, right_half)
        
        # compare and sort then combine arrays into on are the return to the caller fuction 
        def combine(left_half, right_half):
            left , right = 0,0
            result = []
            while left < len(left_half) and right < len(right_half):
                if left_half[left] > right_half[right]:
                    result.append(right_half[right])
                    right +=1
                else:
                    result.append(left_half[left])
                    left += 1
            
            result.extend(left_half[left:])
            result.extend(right_half[right:])
            return result

        return Divide(0 , len(nums)-1 , nums)
