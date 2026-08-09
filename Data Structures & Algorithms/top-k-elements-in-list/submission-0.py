class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # keep track of numbers like prev solution
        tracker = {}
        for num in nums:
            if num not in tracker:
                tracker[num] = 1
            else:
                tracker[num] += 1
        
        # create buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        # store the numbers based on their freq
        # E.G: for the input nums = [1,2,2,3,3,3,7,7]
        # buckets[2] = [2,7]
        for num, freq in tracker.items():
            buckets[freq].append(num)
        
        result = []
        # iterate through each frequency
        for i in range(len(buckets) - 1, 0, -1):
            # go through each number with the frequency i
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result