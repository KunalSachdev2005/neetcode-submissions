class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftPtr = 0
        rightPtr = len(height) - 1

        max_area = 0

        while leftPtr < rightPtr:
            curr_area = (rightPtr - leftPtr) * min(height[leftPtr], height[rightPtr])
            max_area = max(max_area, curr_area)

            if height[leftPtr] < height[rightPtr]:
                leftPtr += 1
            else:
                rightPtr -= 1
        
        return max_area
        