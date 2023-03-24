# TC - TIme compelexity of O(n*m), where n is the number of coins and m is the target amount.
# SC - the  space complexity is also O(n * m) . we are creating a 2D


class Solution:
    def coinChange(self, coins, amount):
        #rows : len(coins) +1
        # coumns: target amount
        dp = [[0 for _ in range(amount+1)] for s in range(len(coins)+1)]
        for j in range(1, amount+1):
            dp[0][j] = amount+1  # amount+1 is infinity here

        for i in range(1, len(coins) + 1):
            for j in range(amount+1):
                if j < coins[i - 1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j], 1 + dp[i][j-coins[i-1]])

        if dp[-1][-1] == amount + 1:
            return -1
        # Backtrack through the DP table to find the coins used to achieve target in min possible ways
        coins_used = []
        i, j = len(coins), amount
        while i > 0 and j > 0:
            if dp[i][j] != dp[i-1][j]:
                coins_used.append(coins[i-1])
                j -= coins[i-1]
            else:
                i -= 1

        print(coins_used)
        return dp[-1][-1]
