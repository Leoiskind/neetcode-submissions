class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        lowest = float('inf')
        highest = float('inf')
        gain = 0
        for price in prices:
            profit = price - lowest
            if profit > gain:
                gain = profit
            if price < lowest:
                lowest = price
            
        return gain
            

            