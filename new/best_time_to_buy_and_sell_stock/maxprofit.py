# tc-o(n)
# sc-O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variables to keep track of the lowest price and maximum profit
        current_low = 0
        lowest = prices[0]

        # Iterate over the prices and update the lowest price and maximum profit
        for price in prices:
            if price < lowest:
                lowest = price
            current_low = max(current_low, price - lowest)

        # Return the maximum profit
        return current_low
