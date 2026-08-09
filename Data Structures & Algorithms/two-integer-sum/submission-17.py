class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            diff = target - num
            shift = idx + 1
            if diff in nums[shift:]:
                return [idx, nums[idx + 1:].index(diff) + shift]