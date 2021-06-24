#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# TAGS: Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # 32 ms, 64.41%. Time: OO(N). Space: O(1)
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        def invert(head, cnt=1):
            prev = None
            node = head
            # flip until right
            while node and cnt <= right:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
                cnt += 1
            head.next = nxt
            return prev

        # Edge Case
        if left == 1:
            return invert(head)

        # Go to node at left
        node = head
        for i in range(2, left):
            node = node.next

        # Flip from left
        node.next = invert(node.next, left)

        return head
# @lc code=end
