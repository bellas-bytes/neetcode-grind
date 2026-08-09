class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in nums]
        for i, num in enumerate(nums):
            for j, val in enumerate(result):
                if i == j:
                    continue
                else:
                    result[j] *= nums[i]
        return result
