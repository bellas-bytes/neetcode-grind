from collections import Counter
import heapq 

class Solution:
    def reorganizeString(self, s: str) -> str:
        letters = Counter(s)

        if any(count > ((len(s) + 1 )// 2) for count in letters.values()):
            return ""
        
        h = []

        for key, value in letters.items():
            heapq.heappush(h, (-value, key))
        
        prev_char = (0, "")
        new_string = []

        for i in range(len(s)):
            curr_char = heapq.heappop(h)

            new_string.append(curr_char[1])

            if prev_char[0] < 0:
                heapq.heappush(h, (prev_char[0] + 1, prev_char[1]))
            prev_char = (curr_char[0], curr_char[1])

        return "".join(new_string)
        

        

        