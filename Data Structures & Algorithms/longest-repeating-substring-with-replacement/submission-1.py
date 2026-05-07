class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        leftPtr = 0
        frequencyMap = {}
        longest = 0

        for rightPtr in range(len(s)):
            frequencyMap[s[rightPtr]] = frequencyMap.get(s[rightPtr], 0) + 1

            windowSize = rightPtr - leftPtr + 1
            maxFreq = max(frequencyMap.values())

            while windowSize - maxFreq > k:
                frequencyMap[s[leftPtr]] -= 1
                leftPtr += 1

                windowSize = rightPtr - leftPtr + 1
                maxFreq = max(frequencyMap.values())

            longest = max(longest, windowSize)
        
        return longest