class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i, num in enumerate(nums):
            diff = target - num

            if diff in nums[i + 1:]:
                diff_idx = nums[i + 1:].index(diff) + i + 1
                return [i,diff_idx ]