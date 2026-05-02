class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        answer = [0] * len(nums)

        runningPrefix = 1
        runningSuffix = 1

        for i in range(n):
            prefix[i] = runningPrefix
            suffix[n - 1 - i] = runningSuffix

            runningPrefix *= nums[i]
            runningSuffix *= nums[n - 1 - i]

        for i in range(n):
            answer[i] = prefix[i] * suffix[i]

        return answer