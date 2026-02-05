class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        cont = dict()
        n = len(matches)

        winner = set()
        losser = set()
        for i in range(n):
            winner.add(matches[i][0])
            losser.add(matches[i][1])
        answer0 = list(winner - losser)

      
        for i in range(n):
            loser = matches[i][1]
            cont[loser] = cont.get(loser,0) + 1
       

        answer1 = [key for key , value in cont.items() if value <2]
        answer1.sort()
        return [answer0, answer1 ]