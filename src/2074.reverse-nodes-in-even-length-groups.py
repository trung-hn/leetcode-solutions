#
# @lc app=leetcode id=2074 lang=python3
#
# [2074] Reverse Nodes in Even Length Groups
#

# @lc code=start
# TAGS: Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Time and Space: O(N)
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next

        # Traverse list and operate
        ptr = 0
        limit = 1
        for i in range(len(vals) + 1):
            if i - ptr == limit or i == len(vals):
                if (i - ptr) % 2 == 0:
                    vals[ptr:i] = reversed(vals[ptr:i])
                ptr = i
                limit += 1

        # Turn it back to linked list
        root = node = ListNode()
        for val in vals:
            node.next = ListNode(val)
            node = node.next
        return root.next
# @lc code=end
