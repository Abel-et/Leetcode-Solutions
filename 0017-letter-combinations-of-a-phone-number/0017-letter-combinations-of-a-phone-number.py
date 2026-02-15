class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        contact = {2:["a","b","c"],3:['d','e','f'],4:['g','h','i'],5:['j','k',"l"],6:['m','n','o'],
                    7:["p",'q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
        
        length_char = len(digits)
        
        if length_char ==1:
            return contact[int(digits[0])]
        
        if length_char == 2:
            val1 = contact[int(digits[0])]
            val2 = contact[int(digits[1])]
            return [f'{val1[i]}{val2[j]}' for i in range(len(val1)) for j in range(len(val2))]
        
        if length_char ==3:
            val1 = contact[int(digits[0])]
            val2 = contact[int(digits[1])]
            val3 = contact[int(digits[2])]
            return [f'{val1[i]}{val2[j]}{val3[k]}'for i in range(len(val1)) for j in range(len(val2)) for k in range(len(val3))]
        if length_char == 4:
            val1 = contact[int(digits[0])]
            val2 = contact[int(digits[1])]
            val3 = contact[int(digits[2])]
            val4 = contact[int(digits[3])]
            return [f'{val1[i]}{val2[j]}{val3[k]}{val4[x]}'for i in range(len(val1)) for j in range(len(val2)) for k in range(len(val3)) for x in range(len(val4))]


        

        