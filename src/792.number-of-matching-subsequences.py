#
# @lc app=leetcode id=792 lang=python3
#
# [792] Number of Matching Subsequences
#

# @lc code=start
# TAGS: Array
# REVIEWME: String


class Solution:
    # Time: O(log(N)*M*L)
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def binary_search(target, arr):
            lo, hi = 0, len(arr) - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid] >= target:
                    hi = mid
                else:
                    lo = mid + 1
            return arr[lo]

        indexes = collections.defaultdict(list)
        for i, c in enumerate(s):
            indexes[c].append(i)

        total = 0
        for word in words:
            prev = -1
            for c in word:
                if not indexes[c]:
                    break
                if prev + 1 > indexes[c][-1]:
                    break
                prev = binary_search(prev + 1, indexes[c])
            else:
                total += 1
        return total

    # 504 ms, 69.58%. Time: O(N + M * L). Space: O(M)
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        pointers = collections.defaultdict(list)
        for i, w in enumerate(words):
            pointers[w[0]].append([i, 1])

        cnt = 0
        for c in s:
            for i, ptr in pointers.pop(c, ()):
                ptr += 1
                if ptr >= len(words[i]):
                    cnt += 1
                else:
                    pointers[words[i][ptr]].append((i, ptr))
        return cnt

    # 396 ms, 87.91%. Time: O(N + M * L). Space: O(M)
    # Same as above but use iterator instead
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        pointers = collections.defaultdict(list)
        for w in words:
            pointers[w[0]].append(iter(w[1:]))
        for c in s:
            for ptr in pointers.pop(c, ()):
                pointers[next(ptr, None)].append(ptr)
        return len(pointers[None])


# @lc code=end
