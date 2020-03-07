# 322. Coin Change
# Medium
#
# 3107
#
# 104
#
# Add to List
#
# Share
# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
# Example 1:
#
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:
#
# Input: coins = [2], amount = 3
# Output: -1
# Note:
# You may assume that you have an infinite number of each kind of coin

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        curr_min = float('inf')
        coins = sorted(coins)[::-1]
        max_index = len(coins) - 1

        def dfs(curr_count, remain, coin_index, min_count):
            coin = coins[coin_index]

            # if remaining amount can be divided by coin,
            # then that's the least amount of coin counts
            if not remain % coin:
                return min(min_count, curr_count + remain // coin)

            # if already at the last coin, return min_count
            if coin_index == max_index:
                return min_count

            # (curr_count + i): number of coins if trying to fill remaining amount with current coin
            # (remain - coin*i): remainder if using current coin
            # (remaining - coin*j)//coins[i + 1]: number of times the next coin can fill into the remaining amount
            # (curr_count + i) + (remaining - coin*j)//coins[i + 1]: number of times current coin and next coin can fit
            for i in range(remain // coin, -1, -1):
                # print('coin_index at:', coin_index)
                # if curr_count + i < min_count: # this is not enough, time limit exceeded, need next line
                if curr_count + i - (remain - coin * i) // -coins[coin_index + 1] < min_count:
                    min_count = min(min_count, dfs(curr_count + i, remain - coin * i, coin_index + 1, min_count))

            return min_count

        min_count = dfs(0, amount, 0, curr_min)

        if min_count == float('inf'):
            return -1
        return min_count