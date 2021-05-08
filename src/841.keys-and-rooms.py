#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
# TAGS: DFS, Graph


class Solution:
    # 60 ms, 94%. Time: O(N^2). Space O(N). Iteration. BFS
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys_acquired = set([0])
        q = [0]
        for i in q:
            for key in rooms[i]:
                if key not in keys_acquired:
                    keys_acquired.add(key)
                    q.append(key)
        return len(keys_acquired) == len(rooms)

    # 60 ms, 94%. Time: O(N^2). Space: O(N). Recursively. DFS
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.keys_acquired = set([0])

        def dfs(room):
            for key in room:
                if key not in self.keys_acquired:
                    self.keys_acquired.add(key)
                    dfs(rooms[key])

        dfs(rooms[0])
        return len(self.keys_acquired) == len(rooms)


# @lc code=end
