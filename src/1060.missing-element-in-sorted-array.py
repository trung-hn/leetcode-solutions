# TAGS: Premium, Binary Search,
# REVIEWME:

class Solution:
    # 312 ms, 60.94%. O(logN * logN), O(1)
    def missingElement(self, A: List[int], k: int) -> int:
        max_val, min_val = A[-1], A[0]
        ln = len(A)

        # Case 1: outside range
        no_missing = max_val - min_val + 1 - ln
        if k > no_missing:
            return max_val + (k - no_missing)

        # Case 2: inside
        lo, hi = A[0], A[-1]
        while lo < hi: # log(N)
            mid = (lo + hi)//2
            index = bisect.bisect_right(A, mid) # log(N)
            no_missing = (mid - min_val + 1) - index
            if no_missing < k:
                lo = mid + 1
            else:
                hi = mid
        return lo
            
    # 300 ms, 85.98%. O(logN), O(1)
    def missingElement(self, A: List[int], k: int) -> int:
        max_val, min_val = A[-1], A[0]
        ln = len(A)

        # Case 1: outside range
        no_missing = max_val - min_val + 1 - ln
        if k > no_missing:
            return max_val + (k - no_missing)

        # Case 2: inside
        lo, hi = 0, len(A) - 1
        while lo < hi: # log(N)
            mid = (lo + hi)//2
            val = A[mid]
            no_missing = (val - min_val + 1) - (mid + 1)
            if no_missing < k:
                lo = mid + 1
            else:
                hi = mid
        return min_val + (k + lo) - 1