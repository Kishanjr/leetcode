# TC O(N log k).
# SC O(k).
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create an empty min-heap
        hp = []

        nk = len(nums) - k + 1

        # Iterate over each element in the input array.
        for num in nums:
            # Push the negative of each element onto the heap so that the largest elements are at the top.
            heappush(hp, -num)

            # If the heap contains more than nk elements, pop the smallest element (i.e. the kth largest element).
            if len(hp) > nk:
                heappop(hp)

        # Return the negative of the kth largest element, since we pushed the negative of each element onto the heap.
        return -hp[0]
