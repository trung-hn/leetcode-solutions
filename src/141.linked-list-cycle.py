#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# TAGS: Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        fast = head.next
        slow = head
        while fast and fast.next:
            if slow == fast: return True
            slow = slow.next
            fast = fast.next.next
        return False
# @lc code=end

