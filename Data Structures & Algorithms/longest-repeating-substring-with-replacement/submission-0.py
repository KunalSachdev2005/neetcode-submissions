class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left_i = 0
        len_longest_substr = 0

        char_count = defaultdict(int)

        for right_i in range(len(s)):
            char_count[s[right_i]] += 1

            max_freq = max(char_count.values())

            # Check if the window is invalid
            while (right_i - left_i + 1 - max_freq) > k:
                char_count[s[left_i]] -= 1
                left_i += 1

            # Update the longest valid substring length
            len_longest_substr = max(len_longest_substr, right_i - left_i + 1)
        
        return len_longest_substr

        # Time: O(n) : right_i traverses all elems. max_freq will need O(26). inner while loop - left_i can move to the right at most n times (one for each character), but each time the while loop runs, it reduces the window size. Thus, the total number of times left_i is incremented across the entire execution of the function is also at most n.
        # Space: O(1)