class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxValue = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                if count > maxValue:
                    maxValue = count
                count = 0
        return max(maxValue, count)