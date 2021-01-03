#
# @lc app=leetcode id=1700 lang=python3
#
# [1700] Number of Students Unable to Eat Lunch
#

# @lc code=start
# TAGS: Array
class Solution:
    # 36 ms, 82.21%. Time: O(N). Space: O(N). First solution, not optimal
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        wants_0 = students.count(0)
        wants_1 = len(students) - wants_0
        queue = collections.deque(students)
        sandwiches = collections.deque(sandwiches)
        while queue:
            if queue[0] == sandwiches[0]:
                sandwiches.popleft()
                if queue.popleft():
                    wants_1 -= 1
                else:
                    wants_0 -= 1
            else:
                if wants_1 == 0 or wants_0 == 0:
                    break
                queue.append(queue.popleft())
        return len(queue)

    # 36 ms, 82.21%. Time: O(N). Space: O(1). Optimal solution
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        wants = [0, 0]
        for student in students:
            wants[student] += 1
        for sandwich in sandwiches:
            if wants[sandwich]:
                wants[sandwich] -= 1
            else: break
        return sum(wants)
# @lc code=end

