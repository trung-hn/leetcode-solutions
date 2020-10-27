#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# TAGS: Linked List, Two Pointers. 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # TAGS: 48 ms, 82.17%. Time: O(N). Space: O(1)
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if not fast or not fast.next:
            return None
        
        node = head
        while node is not slow:
            node = node.next
            slow = slow.next
        return slow
# @lc code=end

