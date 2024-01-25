#
# @lc app=leetcode id=636 lang=python3
#
# [636] Exclusive Time of Functions
#


# @lc code=start
# TAGS: Array, Stack
class Solution:
    # 70 ms, 78.85%
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n  # [3, 4]
        cur_fid = None  # 0
        prev_time = 0  # 6
        stack = []  # None,
        for log in logs:
            fid, status, time = log.split(":")
            fid = int(fid)
            time = int(time)

            # update timer for curent fid
            if cur_fid is not None:
                ans[cur_fid] += time - prev_time

            if status == "start":
                # put on stack, change current fid
                stack.append(cur_fid)
                cur_fid = fid
                prev_time = time

            if status == "end":
                # pop from stack, cahnge current fid
                ans[cur_fid] += 1
                cur_fid = stack.pop()
                prev_time = time + 1

        return ans

    # 70 ms, 78.85%
    # Time and Space: O(N)
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """Same as above but cleaner"""
        ans = [0] * n
        stack = [[0, 0]]
        for log in logs:
            fid, status, time = log.split(":")
            fid, time = int(fid), int(time)

            if status == "start":
                ans[stack[-1][0]] += time - stack[-1][1]
                stack.append([fid, time])
            else:
                ans[stack[-1][0]] += time - stack[-1][1] + 1
                stack.pop()
                stack[-1][1] = time + 1  # Update prev time when status is "end"
        return ans


# @lc code=end
