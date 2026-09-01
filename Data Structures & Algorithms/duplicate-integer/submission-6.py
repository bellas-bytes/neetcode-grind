class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_count = set(nums)

        return not len(nums) == len(num_count)

       