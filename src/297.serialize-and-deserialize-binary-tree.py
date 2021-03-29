#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# TAGS: Tree, Design
import collections
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    """
    Use Leetcode format
    """
    # 116 ms 70.46%. Time and Space: O(N)

    def serialize(self, root):
        # Convert tree to string
        results = []
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if not node:
                results.append("null")
                continue
            results.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        return " ".join(results)

    def deserialize(self, data):
        # Convert String to Tree
        def pop_data(data):
            val = data.popleft()
            return TreeNode(val) if val != "null" else None

        if not data:
            return None
        data = data.split(" ")
        data = collections.deque(data)
        root = pop_data(data)
        q = [root]
        while data:
            nxt_q = []
            for node in q:
                if not node:
                    continue
                node.left = pop_data(data)
                node.right = pop_data(data)
                nxt_q.append(node.left)
                nxt_q.append(node.right)
            q = nxt_q
        return root
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
