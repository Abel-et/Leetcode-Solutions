# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == [] or lists[0] == []:
            return 

        # put all lists into arr
        arr = []
        for link in lists:
            current = link
            while current:
                arr.append(current.val)
                current = current.next

        if not arr :
            return None
            
        # now apply merge sort , 
        def divide(left, right, arr):
            if left > right:
                return []
            if left == right:
                return [arr[left]]

            mid = left + (right - left)//2
            left_part  = divide(left, mid , arr)
            right_part = divide(mid+1, right , arr)

            return combine(left_part, right_part)



        def combine(left, right):
            result = []
            i , j = 0 , 0

            while i < len(left) and j < len(right) : 
                if left[i] > right[j]:
                    result.append(right[j])
                    j += 1
                else:
                    result.append(left[i])
                    i += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result

        # call the merge sort function 
        result = divide(0 , len(arr)-1, arr)

        dummy = ListNode()
        current = dummy
        # conveting the sorted arr into linked list
        for num in result:
            current.next = ListNode(num)
            current = current.next
        
        return dummy.next