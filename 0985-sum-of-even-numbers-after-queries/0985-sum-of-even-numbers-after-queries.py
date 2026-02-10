class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total = 0
        arr = []
        for i in nums:
            if i%2 == 0 :
                total += i
        
        # traversing each element of queries array to get the value and indeices
        for i in range(len(queries)):
            val, index = queries[i][0], queries[i][1]
            curr = nums[index]

            # check the element before added up if it is even and the comming val is even add the val to total
            if curr%2 == 0 and val%2 ==0:
                nums[index] = (val + curr)
                total += val
                arr.append(total)

            elif curr%2 == 1 and val%2 == 1:
                nums[index] = (val + curr)
                total += (val + curr)
                arr.append(total)
            elif curr%2 == 0 and val%2 == 1:
                nums[index] = (val + curr)
                total -= curr
                arr.append(total)
            else:
                nums[index] = (val + curr)
                arr.append(total)
                continue
        return arr


