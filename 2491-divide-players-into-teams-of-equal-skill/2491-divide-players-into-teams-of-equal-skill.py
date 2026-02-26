class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        s = []
        i,j = 0,len(skill)-1
        prev = 0
        total = 0
        skill.sort()

        while i < j:
            s.append((skill[i], skill[j]))
            i+=1
            j-=1
            if len(s) == 1:
                continue
            else:
                prev = i-2
                if sum(s[prev]) != sum(s[-1]):
                    return -1
                else:
                    prod = s[-1][0] * s[-1][1]
                    total +=prod
        return total +(s[0][0]*s[0][1])
        

