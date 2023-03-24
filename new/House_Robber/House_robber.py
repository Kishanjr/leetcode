class Solution:
    def rob(self, nums: List[int]) -> int:
        p = 0
        cp = 0

        for i in nums:
            temp = cp
            cp = max(p + i, cp)
            p = temp
        return cp
