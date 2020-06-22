# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 72 ms, 76.4%
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        cnt = 0
        flag = True
        node = prev = head
        while node:
            nxt = node.next
            cnt += 1
            if flag:
                prev.next = node
                prev = node
                if cnt == m:
                    cnt = 0
                    flag = not flag
            else:
                prev.next = None
                if cnt == n:
                    cnt = 0
                    flag = not flag
            
            node = nxt
        return head