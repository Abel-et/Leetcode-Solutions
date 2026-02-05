class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        i ,j = 0 ,0
        col = {}
        while i < len(list1) and j < len(list1):
            current = list1[i]
            if current in list2:
                col[current] = list2.index(current) + i
                i+=1
                j+=1
            else:
                i+=1
                j+=1
        minValue = min(col.values())
        answer = [key for key,value in col.items() if value == minValue]
        return answer