class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # count max number of coin that can i get 
        max_num_coins = 0
        
        # sorting based on their decreasing order
        piles.sort(reverse=True)

        # tell how much coin do i get from the given coins
        n = len(piles)//3
        
        # iterate 2n times and get an conis
        for i in range(1,2*n,2):
            max_num_coins += piles[i]
        return max_num_coins