#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# TAGS: Sort, Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time: O(N^2). Space: O(N)
    def insertionSortList(self, head: ListNode) -> ListNode:
        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next
        
        for i in range(len(nodes) - 1):
            while nodes[i].val > nodes[i + 1].val and i >= 0:
                nodes[i].val, nodes[i + 1].val = nodes[i + 1].val, nodes[i].val
                i -= 1
        return head
                
    # Time: O(N^2). Space: O(1)
    def insertionSortList(self, head: ListNode) -> ListNode:
        pseudo_head = ListNode()
        curr = head
        while curr:
            # At each iteration, we insert an element into the resulting list.
            prev_node = pseudo_head
            next_node = prev_node.next
            # find the position to insert the current node
            while next_node:
                if curr.val < next_node.val:
                    break
                prev_node = next_node
                next_node = next_node.next

            next_iter = curr.next
            # insert the current node to the new list
            curr.next = next_node
            prev_node.next = curr

            # moving on to the next iteration
            curr = next_iter

        return pseudo_head.next
# @lc code=end

