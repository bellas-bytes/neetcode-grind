from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks = Counter(tasks)
        h = []
        queue = []

        for key, value in tasks.items():
            heapq.heappush(h, (-value, key))
        
        time = 0

        while len(queue) != 0 or len(h) != 0:
            time += 1
            if len(queue) != 0 and queue[0][0] == time:
                ready_task = queue.pop(0)
                heapq.heappush(h, (ready_task[1], ready_task[2]))
            if len(h) != 0:
                count, key = heapq.heappop(h)
                count += 1

                if count < 0:
                    queue.append(((time + n + 1), count, key))

        return time