class Solution:
    def robone(self, nums: List[int]) -> int:

        dp = []

        if len(nums) >= 1:
            dp.append(nums[0])

        if len(nums) > 1:
            dp.append(max(nums[0], nums[1]))

        for i in range(2, len(nums)):
            dp.append(max((nums[i]+dp[i-2]), dp[i-1]))
            print(dp)

        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]

        return max(self.robone(nums[1:]), self.robone(nums[:-1]))
