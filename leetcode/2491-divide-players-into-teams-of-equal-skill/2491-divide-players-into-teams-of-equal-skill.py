class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        ans = 0
        unique = set()
        skill.sort()
        print(skill)
        left ,right  = 0 , len(skill)-1

        while left < right:
            prod = skill[left] * skill[right]
            add = skill[left] + skill[right]
            unique.add(add)
            ans += prod
            if len(unique) > 1:
                return -1
            left +=1
            right -=1
        
        
        return ans