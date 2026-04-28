class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPtr = 0
        rightPtr = len(numbers) - 1

        while leftPtr < rightPtr:
            if numbers[leftPtr] + numbers[rightPtr] > target:
                rightPtr -= 1
            elif numbers[leftPtr] + numbers[rightPtr] < target:
                leftPtr += 1
            else:
                return [leftPtr+1, rightPtr+1]