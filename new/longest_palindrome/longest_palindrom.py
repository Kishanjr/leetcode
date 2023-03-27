class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashset = set()
        count = 0
        for string_val in s:
            if string_val not in hashset:
                hashset.add(string_val)
            else:
                hashset.remove(string_val)
                count = count + 2

        if len(hashset) != 0:
            count = count + 1
        return count
