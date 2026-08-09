class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numMap = {}

        for num in nums:
            if num not in numMap.keys():
                numMap[num] = 1
            else:
                return True
        return False