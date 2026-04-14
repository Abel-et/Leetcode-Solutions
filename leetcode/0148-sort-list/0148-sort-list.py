# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # check if the head is not empty
        if head is None:
            return

        # convert the give  linked list in to list(arr)
        arr = []
        current = head
        
        while current :
            arr.append(current.val)
            current = current.next
        print(arr)

        # perfomed the divide function in merg sort
        def divide(left , right ,arr):
            if left == right:
                return [arr[left]]
            mid = left + (right - left)//2
            left_part = divide(left , mid , arr)
            right_part = divide(mid +1, right, arr)

            return combine(left_part, right_part)

        # combinet the divided arr
        def combine(left , right):
            result = []
            i , j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] > right[j]:
                    result.append(right[j])
                    j+=1
                else:
                    result.append(left[i])
                    i +=1
            result.extend(left[i:])
            result.extend(right[j:])
            return result

        result = divide(0 , len(arr)-1 , arr)
        
        # conveting the given arr result to linked list
        dummy = ListNode()
        conveter = dummy
        for num in result:
            conveter.next = ListNode(num)
            conveter = conveter.next

        return dummy.next
        