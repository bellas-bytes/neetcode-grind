class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffArray = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in diffArray:
                return [diffArray[diff], i]
            else:
                diffArray[num] = i