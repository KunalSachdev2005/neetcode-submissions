class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        leftPtr = 0
        seenChars = set()
        maxLength = 0

        for rightPtr in range(n):
            currChar = s[rightPtr]

            while currChar in seenChars:
                seenChars.remove(s[leftPtr])
                leftPtr+= 1

            seenChars.add(currChar)
            maxLength = max(maxLength, rightPtr - leftPtr + 1)

        return maxLength    