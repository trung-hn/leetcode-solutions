#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#

# @lc code=start
# TAGS: BFS
# REVIEWME: BFS


class Solution:
    # Time and Space: O(N^2*D^N), N is number of digits (4). D is 0 to 9 (10)
    # Complexity break down:
    # D^N combinations
    # For each combination, there are N ways to turn, for each way, string slicing takes O(N)
    # 704 ms, 43%. 1 directional bfs
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        q = [("0000", 0)]
        for seq, depth in q:
            if seq in visited:
                continue
            visited.add(seq)
            if seq == target:
                return depth
            for i, c in enumerate(seq):
                q.append(
                    (seq[:i] + f"{(int(c) + 1) % 10}" + seq[i + 1:], depth + 1))
                q.append(
                    (seq[:i] + f"{(int(c) - 1) % 10}" + seq[i + 1:], depth + 1))
        return -1

    # 288 ms, 95%. 2 directional bfs
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        heads = set(["0000"])
        tails = set([target])
        steps = 0
        q = []
        while heads or tails:
            temp = set()
            for seq in heads:
                if seq in tails:
                    return steps
                if seq in deadends:
                    continue
                deadends.add(seq)
                for i, c in enumerate(seq):
                    s1 = seq[:i] + f"{(int(c) + 1) % 10}" + seq[i + 1:]
                    s2 = seq[:i] + f"{(int(c) - 1) % 10}" + seq[i + 1:]
                    temp.add(s1)
                    temp.add(s2)
            steps += 1
            heads = tails
            tails = temp
        return -1

# @lc code=end
