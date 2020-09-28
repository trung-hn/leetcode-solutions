#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
# TAGS: Graph, Union Find
# REVIEWME: Graph, Union Find
import functools
class Solution:
    # Graph solution. look for path with dfs
    # Let N be the number of input equations and M be the number of queries.
    # Time: O(M * N). Space: O(N)
    # 20 ms, 98%
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        # DFS search for path and return the product of path. 
        def search(node, target, visited=set()):
            if node in visited: return 0
            if (node, target) in pair_values:
                return pair_values[(node, target)]
            visited.add(node)
            for nxt in edges[node]:
                rv = search(nxt, target, visited)
                if rv: return rv * pair_values[(node, nxt)]
            visited.remove(node)
            return 0
        
        edges = collections.defaultdict(list)
        pair_values = {}
        all_letters = set()
        for (frm, end), val in zip(equations, values):
            edges[frm].append(end)
            edges[end].append(frm)
            all_letters |= set([frm, end])
            pair_values[(frm, end)] = val
            pair_values[(end, frm)] = 1 / val
        
        ans = []
        for a, b in queries:
            if a not in all_letters or b not in all_letters:
                ans.append(-1.0)
            elif a == b:
                ans.append(1.0)
            else:
                visited = set()
                rv = search(a, b, visited)
                ans.append(rv if rv else -1)
        return ans
    
    # Union Find solution from official solution. 
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        gid_weight = {}

        def find(node_id):
            if node_id not in gid_weight:
                gid_weight[node_id] = (node_id, 1)
            group_id, node_weight = gid_weight[node_id]
            # The above statements are equivalent to the following one
            #group_id, node_weight = gid_weight.setdefault(node_id, (node_id, 1))

            if group_id != node_id:
                # found inconsistency, trigger chain update
                new_group_id, group_weight = find(group_id)
                gid_weight[node_id] = \
                    (new_group_id, node_weight * group_weight)
            return gid_weight[node_id]

        def union(dividend, divisor, value):
            dividend_gid, dividend_weight = find(dividend)
            divisor_gid, divisor_weight = find(divisor)
            if dividend_gid != divisor_gid:
                # merge the two groups together,
                # by attaching the dividend group to the one of divisor
                gid_weight[dividend_gid] = \
                    (divisor_gid, divisor_weight * value / dividend_weight)

        # Step 1). build the union groups
        for (dividend, divisor), value in zip(equations, values):
            union(dividend, divisor, value)

        results = []
        # Step 2). run the evaluation, with "lazy" updates in find() function
        for (dividend, divisor) in queries:
            if dividend not in gid_weight or divisor not in gid_weight:
                # case 1). at least one variable did not appear before
                results.append(-1.0)
            else:
                dividend_gid, dividend_weight = find(dividend)
                divisor_gid, divisor_weight = find(divisor)
                if dividend_gid != divisor_gid:
                    # case 2). the variables do not belong to the same chain/group
                    results.append(-1.0)
                else:
                    # case 3). there is a chain/path between the variables
                    results.append(dividend_weight / divisor_weight)
        return results
# @lc code=end

