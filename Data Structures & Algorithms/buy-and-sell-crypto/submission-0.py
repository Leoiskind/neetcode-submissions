class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = len(prices) -1
        sell = []

        maxSell = 0
        for i in range(len(prices)):
            if prices[-i-1] > maxSell:
                maxSell = prices[-i-1]
            sell.append(maxSell)
        
        print(sell)
        maxProfit = 0
        for i in range(len(prices)):
            profit = sell[-i-1] - prices[i]
            if profit>maxProfit:
                maxProfit = profit
        
        return maxProfit
