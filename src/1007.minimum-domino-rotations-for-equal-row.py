#
# @lc app=leetcode id=1007 lang=python3
#
# [1007] Minimum Domino Rotations For Equal Row
#

# @lc code=start
# TAGS: Greedy, Array
class Solution:
    # 1444 ms, 22.41%. Time: O(N*6). Space: O(N)
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def number_in_dominoes(A, B, target):
            setA = set(i for i, v in enumerate(A) if v == target)
            setB = set(i for i, v in enumerate(B) if v == target)
            return setA, setB
        
        smallest = float('inf')
        for target in range(1, 7):
            setA, setB = number_in_dominoes(A, B, target)
            if len(setA | setB) == len(A):
                if len(setA) < len(setB):
                    shorter, longer = setA, setB
                else:
                    shorter, longer = setB, setA
                smallest = min(smallest, len(shorter - longer))
        return smallest if smallest <= len(A) else -1
    
    # 1116 ms, 82.28%. Slightly more optimized
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def number_in_dominoes(A, B, target):
            setA = set(i for i, v in enumerate(A) if v == target)
            setB = set(i for i, v in enumerate(B) if v == target)
            return setA, setB
        
        counter = collections.Counter(A + B)
        nums = [num for num, freq in counter.items() if freq >= len(A)]
        
        smallest = float('inf')
        for target in nums:
            setA, setB = number_in_dominoes(A, B, target)
            if len(setA | setB) == len(A):
                if len(setA) < len(setB):
                    shorter, longer = setA, setB
                else:
                    shorter, longer = setB, setA
                smallest = min(smallest, len(shorter - longer))
        return smallest if smallest <= len(A) else -1
    
    # From article. Greedy
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def check(x):
            """
            Return min number of swaps 
            if one could make all elements in A or B equal to x.
            Else return -1.
            """
            # how many rotations should be done
            # to have all elements in A equal to x
            # and to have all elements in B equal to x
            rotations_a = rotations_b = 0
            for i in range(n):
                # rotations coudn't be done
                if A[i] != x and B[i] != x:
                    return -1
                # A[i] != x and B[i] == x
                elif A[i] != x:
                    rotations_a += 1
                # A[i] == x and B[i] != x    
                elif B[i] != x:
                    rotations_b += 1
            # min number of rotations to have all
            # elements equal to x in A or B
            return min(rotations_a, rotations_b)
    
        n = len(A)
        rotations = check(A[0]) 
        # If one could make all elements in A or B equal to A[0]
        if rotations != -1 or A[0] == B[0]:
            return rotations 
        # If one could make all elements in A or B equal to B[0]
        else:
            return check(B[0])
# @lc code=end

