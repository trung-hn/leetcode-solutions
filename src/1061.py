# TAGS: DFS, Union Find
# REVIEWME: Union Find
class Solution:
    # 44 ms, 66.18%. Time and Space: O(N)
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        class UF:
            def __init__(self):
                self.array = list(range(26))

            def union(self, parent, child):
                parent = self.find(parent)
                child = self.find(child)
                if parent > child: 
                    parent, child = child, parent
                self.array[child] = parent

            def find(self, value): # find and assign parent
                if value != self.array[value]:
                    parent = self.array[value]
                    self.array[value] = self.find(parent)
                return self.array[value]

        disjoint_set = UF()
        for c1, c2 in zip(A, B):
            c1 = ord(c1) - ord('a')
            c2 = ord(c2) - ord('a')
            disjoint_set.union(c1, c2)

        ans = []
        for c in S:
            index = ord(c) - ord('a')
            parent = disjoint_set.find(index)
            ans.append(chr(parent + ord('a')))

        return "".join(ans)