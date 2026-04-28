class Solution:
    def isValid(self, s: str) -> bool:
        open_parentheses_stack = []
        parentheses_hash = {'(':')', '{':'}', '[':']'}
        for bracket in s:
            if bracket in parentheses_hash.keys():
                open_parentheses_stack.append(bracket)
            else:
                if not open_parentheses_stack or bracket != parentheses_hash[open_parentheses_stack.pop()]:
                    return False
        return not open_parentheses_stack

        # Time: O(n)
        # Space: O(n)
        