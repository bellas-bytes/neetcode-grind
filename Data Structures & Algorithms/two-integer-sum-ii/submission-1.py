class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        final = [0, 0]

        for i in range (0, len(numbers)):
            for j in range (1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    final[0] = i + 1
                    final[1] = j + 1
                    return final

        