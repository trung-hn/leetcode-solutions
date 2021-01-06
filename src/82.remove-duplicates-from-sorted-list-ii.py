#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# TAGS: Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Space O(N) would be easy
    # 40 ms, 71.84%. Time: O(N). Space: O(1)
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        
        duplicate = False
        rv = dummy = ListNode(None)
        node = head
        while node and node.next:
            if node.val == node.next.val:
                duplicate = True
            elif duplicate and node.val != node.next.val:
                duplicate = False
            elif not duplicate:
                dummy.next = node
                dummy = dummy.next
            if not node.next.next and not duplicate:
                dummy.next = node.next
                dummy = dummy.next
            node = node.next
        dummy.next = None
        return rv.next
    
    # Article Solution
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # sentinel
        sentinel = ListNode(0, head)

        # predecessor = the last node 
        # before the sublist of duplicates
        pred = sentinel
        
        while head:
            # if it's a beginning of duplicates sublist 
            # skip all duplicates
            if head.next and head.val == head.next.val:
                # move till the end of duplicates sublist
                while head.next and head.val == head.next.val:
                    head = head.next
                # skip all duplicates
                pred.next = head.next 
            # otherwise, move predecessor
            else:
                pred = pred.next 
                
            # move forward
            head = head.next
            
        return sentinel.next
# @lc code=end

