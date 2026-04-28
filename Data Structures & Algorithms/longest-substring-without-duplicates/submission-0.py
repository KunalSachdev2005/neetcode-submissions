class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_i = 0
        right_i = 0
        len_longest_substr = 0

        seen_set = set()

        while right_i < len(s):

            if s[right_i] not in seen_set:
                seen_set.add(s[right_i])
                len_longest_substr = max(len_longest_substr, right_i - left_i + 1)
                right_i += 1
            else:
                seen_set.remove(s[left_i])
                left_i += 1
        
        return len_longest_substr

        # Time: O(n)
        # Space: O(n)

        