#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start
# TAGS: Stack, Greedy
# REVIEWME: Stack, Greedy, Tricky, Hard
import collections
class Solution:
    # LTE. Time: > O(2^N)
    def removeDuplicateLetters(self, s: str) -> str:
        
        pos = collections.defaultdict(list)
        for i, c in enumerate(s):
            pos[c].append(i)
            
        self.indexes = [None] * 26
        self.ans = 'z' * 26
        def dfs(letter='a'):
            if letter == '{':
                rv = combine_letters()
                self.ans = min(rv, self.ans)
                return
                
            if not pos[letter]:
                dfs(chr(ord(letter) + 1))
            else:
                for i in pos[letter]:
                    self.indexes[ord(letter) - ord('a')] = i
                    dfs(chr(ord(letter) + 1))
        
        def combine_letters():
            indexes = [(index, string.ascii_lowercase[i]) for i, index in enumerate(self.indexes) if index is not None]
            return ''.join(c for index, c in sorted(indexes))
        dfs()
        return self.ans




    # 36 ms, 73.93%. From article. Using Stack. Time: O(N). Space: O(26) = O(1)
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurence = {c:i for i, c in enumerate(s)}
        
        seen = set()
        stack = []
        for i, c in enumerate(s):
            # we can only try to add c if it's not already in our solution
            # this is to maintain only one of each character
            if c in seen: continue
            # if the last letter in our solution:
            #    1. exists
            #    2. is greater than c so removing it will make the string smaller
            #    3. it's not the last occurrence
            # we remove it from the solution to keep the solution optimal
            while stack and c <= stack[-1] and i < last_occurence[stack[-1]]:
                seen.discard(stack.pop())
            stack.append(c)                
            seen.add(c)
        return ''.join(stack)

    # From article. Greedy. Time and Space: O(N)
    def removeDuplicateLetters(self, s: str) -> str:

        # find pos - the index of the leftmost letter in our solution
        # we create a counter and end the iteration once the suffix doesn't have each unique character
        # pos will be the index of the smallest character we encounter before the iteration ends
        c = collections.Counter(s)
        pos = 0
        for i in range(len(s)):
            if s[i] < s[pos]: pos = i
            c[s[i]] -=1
            if c[s[i]] == 0: break
        # our answer is the leftmost letter plus the recursive call on the remainder of the string
        # note we have to get rid of further occurrences of s[pos] to ensure that there are no duplicates
        return s[pos] + self.removeDuplicateLetters(s[pos:].replace(s[pos], "")) if s else ''

        


# @lc code=end

