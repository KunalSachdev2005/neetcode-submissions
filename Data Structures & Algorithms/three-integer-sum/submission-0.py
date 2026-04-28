class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)

        triplets = []

        TARGET = 0

        for i in range(len(sortedNums) - 2):
            leftPtr = i + 1
            rightPtr = len(sortedNums) - 1

            if i > 0 and sortedNums[i-1] == sortedNums[i]:
                continue
            
            while leftPtr < rightPtr:

                tripletSum = sortedNums[i] + sortedNums[leftPtr] + sortedNums[rightPtr]
                
                if tripletSum > TARGET:
                    rightPtr -= 1
                
                elif tripletSum < TARGET:
                    leftPtr += 1

                else:
                    triplets.append([sortedNums[i], sortedNums[leftPtr], sortedNums[rightPtr]])

                    leftPtr += 1
                    rightPtr -= 1
                    
                    while leftPtr < rightPtr and sortedNums[leftPtr] == sortedNums[leftPtr - 1]:
                        leftPtr += 1

                    while leftPtr < rightPtr and sortedNums[rightPtr] == sortedNums[rightPtr + 1]:
                        rightPtr -= 1

        return triplets