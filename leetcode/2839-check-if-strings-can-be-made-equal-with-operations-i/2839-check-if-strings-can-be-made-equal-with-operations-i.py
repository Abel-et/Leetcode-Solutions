class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # change the string value into list for flexibilty to preform swap
        a, b = [l for l in s1], [k for k in s2]

        # chech all elements of  s1 in s2
        for i in a:
            if i not in b:
                return False
        
        # helper function which check if the passed to array are identical or not
        def check(arr1, arr2):
            for i in range(len(arr1)):
                if arr1[i] != arr2[i]:
                    return False
            return True
        if check(a,b):
            return True

        # i use for the staring index, pointer check both of two list index elements and first bool use the i value is take or not
        i , pointer , first = 0 ,0 ,False

        while pointer < len(s1):
            
            # if on the given index on both two element are no equal 
            if a[pointer] != b[pointer]:
                # and first is not taken give the current pointer element to i and update i value
                if not first:
                    i = pointer
                    first = True
                    pointer +=1
                
                # if the two the i value and ponter value has not one element in between update pointer
                elif pointer - i != 2:
                    pointer +=1
                else:
                    # swap and reset the value of 
                    a[pointer], a[i] = a[i], a[pointer]
                    if check(a,b):
                        return True
                    pointer = i+1
                    first = False
            else:
                pointer +=1
            
        return False
        