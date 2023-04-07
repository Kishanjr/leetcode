#TC - O(n)
#sc - O(n)
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # create a dictionary 'freq' to store the frequency count of each element in 'nums'
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        # create a bucket list to store elements with the same frequency together
        # since the maximum frequency cannot be more than the length of the input list 'nums',
        # we can create a bucket list of length n+1 where n is the length of 'nums'
        bucket = [[] for _ in range(len(nums)+1)]

        # add the elements in 'freq' to the bucket list according to their frequency count
        for key, value in freq.items():
            bucket[value].append(key)

        # create a list 'result' to store the k most frequent elements
        result = []

        # iterate from the end of the bucket list to the beginning
        # and add the elements to the 'result' list until it has k elements
        for i in range(len(bucket)-1, 0, -1):
            if bucket[i]:
                result += bucket[i]
                k -= len(bucket[i])
            if k == 0:
                break

        return result
