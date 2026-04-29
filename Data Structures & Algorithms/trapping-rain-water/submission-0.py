class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        totalWater = 0

        while left < right:
            currLeftHeight = height[left]
            currRightHeight = height[right]

            leftMax = max(leftMax, currLeftHeight)
            rightMax = max(rightMax, currRightHeight)

            if leftMax <= rightMax:
                totalWater += leftMax - currLeftHeight
                left += 1
            else:
                totalWater += rightMax - currRightHeight
                right -= 1
        
        return totalWater
