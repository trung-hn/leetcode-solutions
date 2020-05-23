#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
# TAGS: String, Backtracking
# REVIEWME:
class Solution:
    # 28 ms, 90%. 
    def generateParenthesis(self, n: int) -> List[str]:
        OP = n-1
        CL = n
        S = [["(", OP, CL]]
        def dfs(S):
            temp = []
            for s, op, cl in S:
                if op >= cl >0:
                    temp.append([s + "(", op-1, cl])
                elif op == 0 and cl:
                    temp.append([s + ")", 0, cl-1])
                elif op < cl: 
                    temp.append([s + "(", op-1, cl])
                    temp.append([s + ")", op, cl-1])
            return dfs(temp) if temp else S
        S = dfs(S)
        return [val[0] for val in S]
    
    # From discussion
    def generateParenthesis(self, n, open=0):
        if n > 0 <= open:
            return ['(' + p for p in self.generateParenthesis(n-1, open+1)] + \
                   [')' + p for p in self.generateParenthesis(n, open-1)]
        return [')' * open] * (not n)
    
    # 32 ms, 77.42%. 
    def generateParenthesis(self, n):
        rv = []
        def gen(sofar='', op=0, cl=0):
            if op == cl == n: 
                rv.append(sofar)
            elif op > n or cl > n or cl > op:
                return
            gen(sofar + "(", op + 1, cl)
            gen(sofar + ")", op, cl + 1)
        gen()
        return rv
# @lc code=end

