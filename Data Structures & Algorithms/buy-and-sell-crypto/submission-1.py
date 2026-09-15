class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProf = 0
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
                print(minPrice)
            
            profit = prices[i] - minPrice

            if profit > maxProf:
                maxProf = profit
        
        return maxProf