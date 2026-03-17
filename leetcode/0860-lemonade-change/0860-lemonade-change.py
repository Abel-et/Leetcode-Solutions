class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five,tewnty,ten  = 0,0,0

        if bills[0] > 5 or not bills:
            return False

        for i in range(len(bills)):
            if bills[i] == 5:
                five +=1
            elif bills[i] == 10:
                if five > 0 :
                    ten +=1
                    five -=1
                else:
                    return False
            else:
                if five >=3 or ten > 0:
                    if ten > 0 and five > 0:
                        tewnty +=1
                        ten-=1
                        five -= 1
                    elif five >=3:
                        five -=3
                        tewnty +=1
                    else:
                        return False
                    
                else:
                    return False
        return True

        