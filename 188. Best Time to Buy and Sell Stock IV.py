#!/usr/bin/env python
"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.

# my solution based on https://discuss.leetcode.com/topic/22245/well-explained-python-dp-with-comments/4
# this code is more elegant with same reasoning https://discuss.leetcode.com/topic/23888/concise-python-solution-with-detailed-explanation-o-kn-time-o-k-space
"""

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or not k: # edge case when prices or k is empty or 0
            return 0

        if k >= len(prices) // 2: # edge case when there's more k than half of prices it reduces to the problem type II, reuse old solution
            profit = 0
            for i in range(len(prices) - 1):
                nextP, currP = prices[i + 1], prices[i]
                if nextP > currP:
                    profit += max(nextP - currP, 0)
            return profit

        buy = [-float('inf')] * k # initialize values to negative
        buy[0] = prices[0] # except the first one
        sell = [0] * k # initialize values to 0
        for p in prices:
            for i in range(k):
                if i == 0: # buy and sell followed this setting from problem type III and stays that way for problem type IV
                    buy[0] = min(buy[0], p) # prices stocks bought at for the first iteration
                    sell[i] = max(sell[i], p - buy[i]) # prices sold hence the profit at the first iteration
                else: # buy and sell always follows this pattern after inspection and trying to generalize from problem type III for k > 1
                    buy[i] = max(buy[i], sell[i - 1] - p) # money left after buying after the first iteration for all k > 1
                    sell[i] = max(sell[i], p + buy[i]) # money left after selling after the first iteration for all k > 1
        return sell[k - 1]
