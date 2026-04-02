class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
    
        # Initialize DP table with -infinity
        # dp[k][i][j] is max coins at (i, j) using k neutralizations
        dp = [[[-float('inf')] * n for _ in range(m)] for _ in range(3)]
        
        # Initialize start cell (0, 0)
        # k=0: Take the value as is
        dp[0][0][0] = coins[0][0]
        # k=1 or k=2: Neutralize if negative, otherwise just take the value
        start_val_neutralized = max(0, coins[0][0]) if coins[0][0] < 0 else coins[0][0]
        dp[1][0][0] = start_val_neutralized
        dp[2][0][0] = start_val_neutralized

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                
                for k in range(3):
                    # Transitions from Top (i-1, j) and Left (i, j-1)
                    for prev_i, prev_j in [(i-1, j), (i, j-1)]:
                        if prev_i >= 0 and prev_j >= 0:
                            # Case 1: Don't neutralize current cell
                            dp[k][i][j] = max(dp[k][i][j], dp[k][prev_i][prev_j] + coins[i][j])
                            
                            # Case 2: Use one neutralization on current cell (if k > 0 and negative)
                            if k > 0 and coins[i][j] < 0:
                                dp[k][i][j] = max(dp[k][i][j], dp[k-1][prev_i][prev_j])
                                
        return max(dp[0][-1][-1], dp[1][-1][-1], dp[2][-1][-1])
            