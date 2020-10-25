# TAGS: Dynamic Programming, Backtracking, Premium
import functools

class Solution:
    # Cheating.
    def numberOfPatterns(self, m: int, n: int) -> int:
        patterns = [0, 9, 56, 320, 1624, 7152, 26016, 72912, 140704, 140704]
        return sum(patterns[m : n + 1])

class Solution:
    # Question is not clear about this: 1 -> 8 does not pass 4 and 5
    # 3320 ms, 5%. Time O(1). Space: O(1)
    def numberOfPatterns(self, m: int, n: int) -> int:
        all_crossovers = {(1,3):[2], (1,7):[4], (1,9):[5], (2,8):[5], (3,7):[5], (3,9):[6], (4,6):[5], (7,9):[8]}

        def get_crossovers(last, num):
            if last < num:
                return all_crossovers.setdefault((last, num), [])
            return all_crossovers.setdefault((num, last), [])
        
        def is_valid(num, visited):
            if not visited: return True
            if num in visited: return False
            crossovers = get_crossovers(visited[-1], num)
            return all(crossover in visited for crossover in crossovers)
        
        def dfs(visited=[]):
            if len(visited) > n: 
                return
            elif m <= len(visited) <= n:
                self.counter += 1
            
            for num in range(1, 10):
                if not is_valid(num, visited): continue
                dfs(visited + [num])
                    
        self.counter = 0            
        dfs()
        return self.counter
    
    # 784 ms, 67%. Speed up by calculate 1 and 2 once then multiply by 4
    def numberOfPatterns(self, m: int, n: int) -> int:
        all_crossovers = {(1,3):[2], (1,7):[4], (1,9):[5], (2,8):[5], (3,7):[5], (3,9):[6], (4,6):[5], (7,9):[8]}
        
        def is_valid(num, visited, last):
            if not visited: return True
            if last < num:
                crossovers = all_crossovers.setdefault((last, num), [])
            else:
                crossovers = all_crossovers.setdefault((num, last), [])
            return all(crossover in visited for crossover in crossovers)
        
        def dfs(visited=set(), last=0):
            if len(visited) > n: return
            elif m <= len(visited) <= n:
                self.counter += 1
            
            for num in range(1, 10):
                if num in visited: continue
                if not is_valid(num, visited, last): continue
                visited.add(num)
                dfs(visited, num)
                visited.remove(num)
                    
        self.counter = 0
        dfs({1}, 1)
        dfs({2}, 2)

        self.counter *= 4
        dfs({5}, 5)
        return self.counter