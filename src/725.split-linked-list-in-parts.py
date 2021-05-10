#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#

# @lc code=start
# TAGS: Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # 32 ms, 93.33%. Time and Space: O(N)
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        if not root:
            return [None] * k
        # Get length
        L = 0
        head = root
        while head:
            head = head.next
            L += 1

        q, r = divmod(L, k)
        ans = []
        node = root
        for _ in range(k):
            ans.append(node)
            for _ in range(q):
                prev = node
                node = node.next
            if r:
                prev = node
                node = node.next
                r -= 1
            prev.next = None
        return ans

# @lc code=end
