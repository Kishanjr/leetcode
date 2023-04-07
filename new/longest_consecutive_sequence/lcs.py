# TC O(N).
# SC O(N).
class Solution(object):
    def longestConsecutive(self, nums):

        numSet = set(nums)

        result = 0
        # Iterate over each number n in the input list.
        for n in nums:
            # If n-1 is not in the numSet, then n is the start of a new consecutive sequence.
            if (n-1) not in numSet:
                # Initialize a variable length to 1, since n is the first number in the sequence.
                length = 1

                while (n+length) in numSet:
                    length += 1
                # If the length of the sequence is greater than the current result, update the result.
                result = max(length, result)
        # Return  the length of the longest consecutive sequence.
        return result
