class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    lst = []
    for i in range(len(nums)):
      if nums[i] not in lst:
        lst.append(target - nums[i])
      else:
        return [lst.index(nums[i]), i]