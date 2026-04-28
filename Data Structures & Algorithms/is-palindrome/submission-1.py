class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_pointer = 0
        right_pointer = len(s) - 1

        while left_pointer < right_pointer:
            if not s[left_pointer].isalnum():
                left_pointer += 1
            elif not s[right_pointer].isalnum():
                right_pointer -= 1
            elif s[left_pointer].lower() == s[right_pointer].lower():
                left_pointer += 1
                right_pointer -= 1
            else:
                return False
        
        return True