from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        i = 0

        for num in nums:
            complement = target - num

            if complement in complements:
                return [complements[complement], i]

            complements[num] = i
            i += 1


# test here
nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target))
