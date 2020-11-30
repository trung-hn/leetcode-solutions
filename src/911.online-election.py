#
# @lc app=leetcode id=911 lang=python3
#
# [911] Online Election
#

# @lc code=start
# TAGS: Binary Search
class TopVotedCandidate:
    """
    600 ms, 85.92%. Time: O(N+QlogN). Time: O(N)
    """
    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.winners = []
        max_sofar = 0
        freq = collections.Counter()
        for person, time in zip(persons, times):
            freq[person] += 1
            if freq[person] >= max_sofar:
                max_sofar = freq[person]
                self.winners.append(person)
            else:
                self.winners.append(self.winners[-1])

    def q(self, t: int) -> int:
        index = bisect.bisect(self.times, t)
        if index == len(self.times) or self.times[index] > t:
            index -= 1
        return self.winners[index]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
# @lc code=end

