class Solution(object):
    def search(self, nums, target):

        l = 0
        h = len(nums)-1

        while l <= h:
            mid = l + (h-l)//2

            if nums[mid] == target:
                return mid

            # left sorted check

            if nums[l] <= nums[mid]:
                #check in wheather in  range
                if nums[l] <= target and target < nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
            # right sorted array check
            else:
                if nums[mid] < target and target <= nums[h]:
                    l = mid + 1
                else:
                    h = mid - 1
        return -1
