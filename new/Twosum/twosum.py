class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        listl = {}
        for i in range(len(nums)):
            num = target - nums[i]
            if num in listl:
                return [listl[num], i]
            listl[nums[i]] = i
        return []
