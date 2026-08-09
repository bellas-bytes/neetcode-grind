class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            diff = target - num
            new_index = idx + 1
            if diff in nums[idx + 1:]:
                return [idx, nums[idx + 1:].index(diff) + idx + 1]