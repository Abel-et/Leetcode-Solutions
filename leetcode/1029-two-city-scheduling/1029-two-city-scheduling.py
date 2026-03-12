class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        cost_differnce = sorted(costs ,key=lambda x : x[0]- x[1])

        result = 0
        for i in range(len(costs)):
            if i < len(costs)//2:
                result +=cost_differnce[i][0]
            else:
                result += cost_differnce[i][1]
        return result