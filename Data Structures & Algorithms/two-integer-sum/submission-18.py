class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in pairs.keys():
                return [pairs[diff], idx]
            else:
                pairs[num] = idx