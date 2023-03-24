class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currect_low = 0

        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            currect_low = max(currect_low, price - lowest)
        return currect_low
