#
# @lc app=leetcode id=2487 lang=python3
#
# [2487] Remove Nodes From Linked List
#


# @lc code=start
# TAGS: Linked List, Stack, Recursion, Monotonic Stack
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 538 ms, 60.17%
    # Time: O(N). Space: O(N)
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        node = head
        while node:
            nums.append(node.val)
            node = node.next

        # Monotonic stack
        stack = []
        for num in nums:
            while stack and stack[-1] < num:
                stack.pop()
            stack.append(num)

        # Construct return list.
        rv = prev = ListNode()
        for num in stack:
            prev.next = ListNode(num)
            prev = prev.next
        return rv.next


# @lc code=end
