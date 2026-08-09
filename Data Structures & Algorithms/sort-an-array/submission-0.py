class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2

        array_1 = self.sortArray(nums[:mid])
        array_2 = self.sortArray(nums[mid:])

        return self.merge(array_1, array_2)
        
    
    def merge(self, arr1: List[int], arr2:List[int]) -> List[int]:
        i = 0
        j = 0
        merged = []

        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1

        while i < len(arr1):
            merged.append(arr1[i])
            i += 1

        while j < len(arr2):
            merged.append(arr2[j])
            j += 1

        return merged