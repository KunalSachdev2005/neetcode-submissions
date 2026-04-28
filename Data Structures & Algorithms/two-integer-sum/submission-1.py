class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashMap = {}
    for i, num in enumerate(nums):
      complement = target - num
      if complement not in hashMap:
        hashMap[num] = i
      else:
        return [hashMap[complement], i]