class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = 0

        for i in range(0, len(nums)):
            diff = target - nums[i]

            new_lst = nums[i + 1:]

            if diff in new_lst:
                idx = new_lst.index(diff) + 1 + i
                return [i, idx]