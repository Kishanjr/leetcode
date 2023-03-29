class Solution:
    def robone(self, nums: List[int]) -> int:

        # Initialize an empty list to store the dynamic programming values
        dp = []

        # Check if the input list has at least one element and add the value to the dp list
        if len(nums) >= 1:
            dp.append(nums[0])

        # Check if the input list has at least two elements and add the maximum value to the dp list
        if len(nums) > 1:
            dp.append(max(nums[0], nums[1]))

        # Iterate over the remaining elements in the input list
        for i in range(2, len(nums)):
            # Calculate the maximum value between the current element plus the value two positions before
            # or the value at the previous position
            dp.append(max((nums[i]+dp[i-2]), dp[i-1]))
            print(dp)

        # Return the last value in the dp list
        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        # Check if the input list is empty or has only one element
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]

        # Return the maximum value between robbing the first house to second last house
        # or robbing the second house to last house
        return max(self.robone(nums[1:]), self.robone(nums[:-1]))

# tc - O(n) where n is the length of the input list
#sc - O(n)
