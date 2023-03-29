class Solution:
    def rob(self, nums: List[int]) -> int:
        # Initialize two variables to keep track of the previous house's max profit (p) and the current house's max profit (cp)
        p = 0
        cp = 0

        # Iterate over each house's profit in the input list
        for i in nums:
            # Store the current cp value in a temporary variable
            temp = cp
            # Update the current cp value to be the maximum between the previous house's profit plus the current house's profit or the previous cp value
            cp = max(p + i, cp)
            # Set the previous house's profit value to be the temporary cp value
            p = temp

        # Return the final cp value, which represents the maximum profit that can be made without robbing adjacent houses
        return cp


#TC - O(n)
#SC - O(1)
