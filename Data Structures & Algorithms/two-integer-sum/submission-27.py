class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = 0

        for index, num in enumerate(nums):
            diff = target - num
            j = index + 1
            if diff in nums[j:]:
                i = nums[j:].index(diff) + index + 1
                return [index, i]