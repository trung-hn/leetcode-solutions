#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
# TAGS: Array, Hash Table, Greedy, Sorting, Heap (Priority Queue), Counting


class Solution:
    # Time: O(N * 27). Space: O(27)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counters = collections.Counter(tasks)
        last_processed = {}

        def get_next_task(steps):
            tasks = reversed(sorted((c, l) for l, c in counters.items()))
            for counter, letter in tasks:
                if letter not in last_processed or last_processed[letter] + n < steps:
                    last_processed[letter] = steps
                    counters[letter] -= 1
                    if counters[letter] == 0:
                        del counters[letter]
                        del last_processed[letter]
                    return 1
            return n + min(last_processed.values()) + 1 - steps

        steps = 0
        while counters:
            steps += get_next_task(steps)
        return steps

    # Greedy
    # Time: O(N). Space: O(27)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counters = list(collections.Counter(tasks).values())
        most = max(counters)  # longest task
        most_count = counters.count(most)  # number of letter with longest task.
        return max(len(tasks), (most - 1) * (n + 1) + most_count)


# @lc code=end
