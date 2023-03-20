class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)-1

        # sort the given list of nums

        nums.sort()

        result = []

        for i in range(n-1):
            if i >= 1 and nums[i] == nums[i-1]:
                continue

            j = i+1
            k = n
            target = -1 * nums[i]

            while j < k:
                if nums[j] + nums[k] == target:
                    result.append([nums[i], nums[j], nums[k]])

                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1

                    j += 1
                    k -= 1

                else:
                    if target < (nums[j]+nums[k]):
                        k -= 1
                    else:
                        j += 1
        return result
