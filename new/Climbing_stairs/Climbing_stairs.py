#tc - O(n)
#sc - O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize variables to keep track of previous steps
        one = 1
        two = 1

        # Check if n is 1, then there is only one way to climb stairs
        if n == 1:
            return 1

        # Loop through steps starting from 2nd step (i.e. n-1 steps)
        for i in range(n-1):
            # Update one and two steps with previous values
            temp = one
            one = one + two
            two = temp

        # Return number of ways to climb n steps (i.e. last value of one)
        return one
