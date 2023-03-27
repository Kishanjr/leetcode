class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_Min = cur_Max = g_Max = nums[0]

        start = 0
        end = 1

        for i in range(1, len(nums)):
            num = nums[i]
            cur_Min, cur_Max = min(
                cur_Min * num, cur_Max * num, num), max(cur_Min * num, cur_Max * num, num)

            if (cur_Max > g_Max):
                g_Max = cur_Max
                end = i+1

        j = end-1
        while j >= 0:
            if nums[j] == 0:
                start = j
                break
            else:
                if g_Max == nums[j]:
                    start = j
                    break
                g_Max = g_Max/nums[j]
            j -= 1

        # nums[start: end] is the maximum product subarray!!
        prod = 1
        for num in nums[start: end]:
            prod *= num
        print(nums[start: end])
        return prod
