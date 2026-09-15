class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxProf = 0

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
                right = left + 1
            else:
                profit = prices[right] - prices[left]
                if profit> maxProf:
                    maxProf = profit
                right += 1
        
        return maxProf
