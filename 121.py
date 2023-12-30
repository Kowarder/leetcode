class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        profit = 0
        p, n = 0, 1
        while n<length:
            if prices[p] < prices[n]:
                money = prices[n] - prices[p]
                profit = max(profit, money)
            else:
                p = n
            n = n + 1
        return profit
