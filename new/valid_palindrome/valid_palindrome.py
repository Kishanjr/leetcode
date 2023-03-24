# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ""

        s = s.lower()

        for i in range(len(s)):
            if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= '0' and s[i] <= '9'):
                palindrome += s[i]

        return palindrome == palindrome[::-1]
