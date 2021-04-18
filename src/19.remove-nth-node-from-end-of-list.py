#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# TAGS: Linked List, Two Pointers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    """
    Approach: 
    1. Move cnt n times
    2. Move both cnt and node at the same time until cnt reach the end. 
    """
    # 36 ms, 43.82%. Time: O(N). Space: O(1)

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = cnt = head
        for _ in range(n):
            cnt = cnt.next

        while cnt:
            if cnt.next:
                node = node.next
                cnt = cnt.next
            else:
                node.next = node.next.next
                return head
        return head.next
# @lc code=end
