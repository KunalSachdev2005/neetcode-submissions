class Solution:
    def isValid(self, s: str) -> bool:

        bracketDict = {'}': '{', ']': '[', ')': '('}        
        stack = list()

        for bracket in s:
            if bracket in ['(', '{', '[']:
                stack.append(bracket)
            else:
                if not stack or stack.pop() != bracketDict[bracket]:
                    return False
        
        return not stack
        