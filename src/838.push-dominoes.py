#
# @lc app=leetcode id=838 lang=python3
#
# [838] Push Dominoes
#

# @lc code=start
# TAGS: Two Pointers
# REVIEWME: Two Pointers, Pythonic
class Solution:
    # 428 ms, 9.94%. Time and Space: O(N)
    def pushDominoes(self, dominoes: str) -> str:
        
        states = [[0, 0] for _ in range(len(dominoes))]
        
        queue = []
        for pos, dom in enumerate(dominoes):
            if dom == "L":
                queue.append([pos, -1 ,0])
            elif dom == "R":
                queue.append([pos, 1 ,0])
        
        queue = collections.deque(queue)
        while queue:
            pos, dir, time = queue.popleft()
            if pos < 0 or pos >= len(dominoes): continue
            if states[pos][0] == 0:
                states[pos] = [dir, time]
                queue.append((pos + dir, dir, time + 1))
            elif 1 in (dir, states[pos][0]) and -1 in (dir, states[pos][0]):
                if states[pos][1] == time:
                    states[pos][0] += dir

        ans = []
        for dir, time in states:
            if dir == -1: ans.append("L")
            elif dir == 1: ans.append("R")
            else: ans.append(".")
        return "".join(ans)
    
    # 148 ms, 62.28%. Time and Space: O(N)
    def pushDominoes(self, dominoes: str) -> str:
        def assign(left, right, value):
            for i in range(left, right):
                states[i] = value
        
        states = list(dominoes)
        fallings = [i for i, dom in enumerate(dominoes) if dom != '.']
        
        for i, (dom1, dom2) in enumerate(zip(fallings, fallings[1:])):
            if dominoes[dom1] == dominoes[dom2]:
                assign(dom1, dom2, dominoes[dom2])
            elif dominoes[dom1] == "R" and dominoes[dom2] == 'L':
                mid = (dom1 + dom2) // 2
                if (dom2 - dom1) % 2:
                    assign(dom1, mid + 1, "R")
                    assign(mid + 1, dom2 + 1, "L")
                else:
                    assign(dom1, mid, "R")
                    assign(mid + 1, dom2 + 1, "L")
        
        if not fallings: return dominoes
        
        if dominoes[fallings[0]] == 'L':
            assign(0, fallings[0], 'L')
            
        if dominoes[fallings[-1]] == 'R':
            assign(fallings[-1], len(states), 'R')
            
        return ''.join(states)
    
    # From article. Similar to above but Very pythonic. Time and Space: O(N)
    def pushDominoes(self, dominoes):
        def cmp(a, b):
            return (a > b) - (a < b) 
        
        symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]

        ans = list(dominoes)
        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            if x == y:
                for k in range(i+1, j):
                    ans[k] = x
            elif x > y: #RL
                for k in range(i+1, j):
                    ans[k] = '.LR'[cmp(k-i, j-k)]

        return "".join(ans)
    
    
    # 244 ms, 31.50%. From article. Calculate force from both sides
    def pushDominoes1(self, dominoes: str) -> str:
        N = len(dominoes)
        force = [0] * N
        f = 0
        for i in range(N):
            if dominoes[i] == 'R': f = N
            elif dominoes[i] == 'L': f = 0
            else: f = max(f-1, 0)
            force[i] += f
        
        f = 0
        for i in range(N-1, -1, -1):
            if dominoes[i] == 'R': f = 0
            elif dominoes[i] == 'L': f = N
            else: f = max(f-1, 0)
            force[i] -= f
        return ''.join("." if f == 0 else 'R' if f > 0 else 'L' for f in force)
# @lc code=end

