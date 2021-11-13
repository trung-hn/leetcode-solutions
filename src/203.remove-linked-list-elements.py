#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start

# TAGS: Linked List, Recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # 64 ms, 90.84%. Time: O(N). Space: O(1)
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = root = ListNode(None, head)
        while head:
            if head.val != val:
                prev.next = head
                prev = prev.next
            head = head.next
        if prev.next and prev.next.val == val:
            prev.next = None
        return root.next
# @lc code=end
