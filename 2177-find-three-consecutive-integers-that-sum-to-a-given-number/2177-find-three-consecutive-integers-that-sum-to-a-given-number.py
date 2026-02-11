class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        mid = num//3
        arr = []

        for i in range(-1,2,1):
            ans = mid + i
            arr.append(ans)
        if sum(arr) == num :
            return arr
        else:
            return []
      
        