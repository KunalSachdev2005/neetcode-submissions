class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)

        if len_s1 > len_s2:
            return False

        s1_count = defaultdict(int)
        s2_count = defaultdict(int)

        for i in range(len_s1):
            s1_count[s1[i]] += 1
            s2_count[s2[i]] += 1
        
        matches = 0
        for char in s1_count:
            if s1_count[char] == s2_count[char]:
                matches += 1
        
        left_i = 0
        for right_i in range(len_s1, len_s2):

            if matches == len(s1_count):
                return True
            
            new_char = s2[right_i]
            s2_count[new_char] += 1
            if new_char in s1:
                if s1_count[new_char] == s2_count[new_char]:
                    matches += 1
                elif s1_count[new_char] + 1 == s2_count[new_char]:
                    matches -= 1
            
            old_char = s2[left_i]
            s2_count[old_char] -= 1
            if old_char in s1:
                if s1_count[old_char] == s2_count[old_char]:
                    matches += 1
                elif s1_count[old_char] - 1 == s2_count[old_char]:
                    matches -= 1
            
            left_i += 1
            print(matches)
        
        return matches == len(s1_count)

        # Time: O(n)
        # Space: O(1) : for s1/s2_count max length is 26 which is constant
