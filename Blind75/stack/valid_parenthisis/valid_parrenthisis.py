class Solution:
    def isValid(self, s: str) -> bool:
        # check if the length of the string is odd, which means brackets can't be balanced
        if len(s) % 2 != 0:
            return False

        # We define a hashmap of matching parentheses and create an empty stack
        hashmap = {'}': '{', ']': '[', ')': '('}
        stack = []

        # loop through each character in the string
        for ch in s:
            # if the character is a closing brackets, check if the top of the stack matches the corresponding open brackets
            if ch in hashmap:
                if stack and stack[-1] == hashmap[ch]:
                    # if it matches, pop the opening brackets from the stack
                    stack.pop()
                else:
                    # if it doesn't match, the brackets is not balanced
                    return False

            # if the character is an opening brackets, we  push it onto the stack
            else:
                stack.append(ch)

        # if all brackets have been matched and popped, the stack will be empty and the brackets is balanced
        return len(stack) == 0
