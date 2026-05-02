class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * len(nums)
        running = 1

        for i in range(n):
            answer[i] = running
            running *= nums[i]

        running = 1

        for i in range(n-1, -1, -1):
            answer[i] *= running
            running *= nums[i]

        return answer