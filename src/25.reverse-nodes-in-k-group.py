#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# TAGS: Linked List, Recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # 52 ms, 56.12%. Time: O(N). Space: O(1)
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def flip(node):
            sav = prev = None
            for _ in range(k):
                # save next-to-last node
                if prev is None:
                    sav = node
                node.next, prev, node = prev, node, node.next

            # put the rest at the end.
            if sav:
                sav.next = node
            return prev

        # get length
        L = 0
        node = head
        while node:
            L += 1
            node = node.next

        # flip
        root = ListNode()
        root.next = head
        node = root
        for i in range(L//k*k):
            if i % k == 0:
                node.next = flip(node.next)
            node = node.next

        return root.next
# @lc code=end
