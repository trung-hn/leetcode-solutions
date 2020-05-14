#
# @lc app=leetcode id=1441 lang=python3
#
# [1441] Build an Array With Stack Operations
#
# TAGS: pythonic,
# @lc code=start
class Solution:
    # 28 ms, 100%
    def buildArray(self, target: List[int], n: int) -> List[str]:
        rv = []
        cnt = 1
        for num in target:
            while cnt < num:
                rv.append("Push")
                if cnt != num:
                    rv.append("Pop")
                cnt += 1
            rv.append("Push")
            cnt += 1
        return rv
    # 32 ms, 77.76%. pythonnic solution using yield
    def buildArray(self, target: List[int], n: int) -> List[str]:
        def build():
            cnt = 1
            for num in target:
                while cnt < num:
                    yield "Push"
                    if cnt != num:
                        yield "Pop"
                    cnt += 1
                yield "Push"
                cnt += 1
        return list(build())
# @lc code=end
