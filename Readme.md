# About:

- This list was initially created for personal use
- Headers and footers of source code are generated from extension `LeetCode` in VSCode

## My profile:
https://leetcode.com/jummyegg/

## Tips to Improve your Skills:

- Solve problem by Topic: when you first started, it is important to understand the topic quickly and solving 10-20 problems per topic is a good way to grasp it.
- If you are using Python and are interested in writing Pythonic code, I created a repo for [Python tips and tricks](https://github.com/trung-hn/python-tips-and-tricks)
- Always aim to get a better solution by reading the dicussion after you successfully solve it. Leetcode's community is amazing, you will learn of lot of tips and tricks to make your code cleaner and faster from the dicussion posts.
- Leetcode has a "Taking Note" system where you can take notes of things you learn for each problem. Make good use of it.
- Leetcode's category of difficulty (Easy, Medium, Hard) is not always correct. My rule of thumb is looking at the acceptance rate. `>55%` means Easy and `<35%` means Hard
- What is correct is the amount of likes and dislikes in a problem. Problems with more dislikes than likes is usually not worth solving. Try a different one.
- When you stuck, there are a few things you can do to give yourself hints:
  - Look at the tag for the problem and see what kind of algorithm or data strucutre is needed to solve it
  - Look at the hints provided by Leetcode
  - Quickly look at the discussion to see what the expected complexity is or the name of the algorithm.
  - Estimate the Time Complexity of the problem based on the input constraints (see next tip)
- You can estimate the Time complexity based on the input constraints:

| input size | estimated time complexity |
|---|---|
| `N <= 10` | `O(N!)` |
| `N <= 20` | `O(2^N)` |
| `N <= 500` | `O(N^3)` |
| `N <= 5000` | `O(N^2)` |
| `N <= 10^6` | `O(N)` or `O(NlogN)` |
| `N > 10^6` | `O(1)` or `O(logN)` |

# Solutions list

| # | Title | Level | Time | Space | Tags | Note | Premium 🔒 |
|---|---|---|---|---|---|---|---|
| 1 | [Two Sum](src/1.two-sum.py) | Easy | O(N) | O(N) | | | |
| 7 | [Reverse Integer](src/7.reverse-integer.py) | Easy | O(log x) | O(1) | | Tricky | |
| 11 | [Container With Most Water](src/11.container-with-most-water.py) | Medium | O(N) | O(1) | Array, Two Pointers | | |
| 12 | [Integer to Roman](src/12.integer-to-roman.py) | Medium | O(N) | O(N) | Math, String | | |
| 13 | [Roman to Integer](src/13.roman-to-integer.py) | Easy | O(N) | O(1) | Math, String | | |
| 15 | [3Sum](src/15.3-sum.py) | Medium | O(N^2) | O(N^2) | Array, Two Pointers | | |
| 17 | [Letter Combinations of a Phone Number](src/17.letter-combinations-of-a-phone-number.py) | Medium | O(2^2) | O(2^N) | String, Backtracking, DFS, Recursion | | |
| 19 | [Remove Nth Node From End of List](src/19.remove-nth-node-from-end-of-list.py) | Medium | O(N) | O(1) | Linked List, Two Pointers | | |
| 20 | [Valid Parentheses](src/20.valid-parentheses.py) | Easy | O(N) | O(N) | String, Stack | | |
| 21 | [Merge Two Sorted Lists](src/21.merge-two-sorted-lists.py) | Easy | O(N) | O(1) | Linked List | | |
| 22 | [Generate Parentheses](src/22.generate-parentheses.py) | Medium | Complex | Complex | String, Backtracking | | |
| 24 | [Swap Nodes in Pairs](src/24.swap-nodes-in-pairs.py) | Medium | O(N) | O(N) | Linked List | | |
| 25 | [Reverse Nodes in k-Group](src/25.reverse-nodes-in-k-group.py) | Hard | O(N) | O(1) | Linked List, Recursion | | |
| 30 | [Substring with Concatenation of All Words](src/30.substring-with-concatenation-of-all-words.py) | Hard | O(NK) | O(K) | Array, Backtracking | | |
| 32 | [Longest Valid Parentheses](src/32.longest-valid-parentheses.py) | Hard | O(N) | O(N) | String, Dynamic Programming | | |
| 34 | [Find First and Last Position of Element in Sorted Array](src/34.find-first-and-last-position-of-element-in-sorted-array.py) | Medium | O(logN) | O(1) | Array, Binary Search | Template for Binary Search | |
| 39 | [Combination Sum](src/39.combination-sum.py) | Medium | O(N^2) | O(N) | Array, Backtracking | | |
| 42 | [Trapping Rain Water](src/42.trapping-rain-water.py) | Hard | O(N) | O(N) | Array, Two Pointers, Dynamic Programming, Stack | | |
| 45 | [Jump Game II](src/45.jump-game-ii.py) | Medium | O(N) | O(1) | Array, Greedy | | |
| 46 | [Permutations](src/46.permutations.py) | Medium | O(N!) | O(N!) | Backtracking | | |
| 47 | [Permutations II](src/47.permutations-ii.py) | Medium | O(N!) | O(N!) | Backtracking | | |
| 48 | [Rotate Image](src/48.rotate-image.py) | Medium | O(N*M) | O(1) | Array | | |
| 51 | [N-Queens](src/51.n-queens.py) | Hard | O(N!) | O(N^2) | Backtracking | | |
| 51 | [N-Queens II](src/52.n-queens-ii.py) | Hard | O(N!) | O(N^2) | Backtracking | | |
| 53 | [Maximum Subarray](src/53.maximum-subarray.py) | Easy | O(N) | O(1) | | | |
| 57 | [Insert Interval](src/57.insert-interval.py) | Hard | O(N) | O(N) | Array, Sort, Greedy | | |
| 59 | [Spiral Matrix II](src/59.spiral-matrix-ii.py) | Medium | O(N^2) | O(N^2) | Array | | |
| 61 | [Rotate List](src/61.rotate-list.py) | Medium | O(N) | O(1) | Linked List, Two Pointers | | |
| 63 | [Unique Paths II](src/63.unique-paths-ii.py) | Medium | O(M*N) | O(M) | Array, Dynamic Programming | | |
| 71 | [Simplify Path](src/71.simplify-path.py) | Medium | O(N) | O(N) | String, Stack | | |
| 72 | [Edit Distance](src/72.edit-distance.py) | Hard | O(N * M) | O(N) | String, Dynamic Programming | | |
| 74 | [Search a 2D Matrix](src/74.search-a-2-d-matrix.py) | Medium | O(logN + logM) | O(1) | Binary Search | | |
| 76 | [Minimum Window Substring](src/76.minimum-window-substring.py) | Hard | O(S+T) | O(S+T) | Hash Table, Two Pointers, String, Sliding Window | | |
| 78 | [Subsets](src/78.subsets.py) | Medium | O(N\*2^N) | O(N\*2^N) | Backtracking, Bit Manipulation | | |
| 80 | [Remove Duplicates from Sorted Array II](src/80.remove-duplicates-from-sorted-array-ii.py) | Medium | O(N) | O(1) | Array, Two Pointers | | |
| 82 | [Remove Duplicates from Sorted List II](src/82.remove-duplicates-from-sorted-list-ii.py) | Medium | O(N) | O(1) | Linked List | | |
| 91 | [Decode Ways](src/91.decode-ways.py) | Medium | O(N) | O(N) | String, Dynamic Programming | | |
| 92 | [Reverse Linked List II](src/92.reverse-linked-list-ii.py) | Medium | O(N) | O(1) | Linked List | | |
| 99 | [Recover Binary Search Tree](src/99.recover-binary-search-tree.py) | Hard | O(N) | O(N) | Tree, DFS | | |
| 100 | [Same Tree](src/100.same-tree.py) | Easy | O(N) | O(H) | Tree, Pythonic | | |
| 102 | [Binary Tree Level Order Traversal](src/102.binary-tree-level-order-traversal.py) | Medium | O(N) | O(N) | Tree, BFS | | |
| 105 | [Construct Binary Tree from Preorder and Inorder Traversal](src/105.construct-binary-tree-from-preorder-and-inorder-traversal.py) | Medium | O(N) | O(N) | Array, Tree, DFS | | |
| 107 | [Binary Tree Level Order Traversal II](src/107.binary-tree-level-order-traversal-ii.py) | Easy | O(N) | O(N) | Tree, BFS | | |
| 111 | [Minimum Depth of Binary Tree](src/111.minimum-depth-of-binary-tree.py) | Easy | O(N) | O(H) | Tree, DFS, BFS | | |
| 114 | [Flatten Binary Tree to Linked List](src/114.flatten-binary-tree-to-linked-list.py) | Medium | O(N) | O(1) | Tree, DFS | | |
| 115 | [Distinct Subsequences](src/115.distinct-subsequences.py) | Medium | O(N) | O(1) | String, Dynamic Programming | | |
| 116 | [Populating Next Right Pointers in Each Node](src/116.populating-next-right-pointers-in-each-node.py) | Medium | O(N) | O(N) | Tree, DFS, BFS | | |
| 119 | [Pascal's Triangle II](src/119.pascals-triangle-ii.py) | Easy | O(k^2) | O(k) | Array | | |
| 121 | [Best Time to Buy and Sell Stock](src/121.best-time-to-buy-and-sell-stock.py) | Easy | O(N) | O(1) | Dynamic Programming | | |
| 122 | [Best Time to Buy and Sell Stock II](src/122.best-time-to-buy-and-sell-stock-ii.py) | Easy | O(N) | O(1) | Array, Greedy | | |
| 125 | [Valid Palindrome](src/125.valid-palindrome.py) | Easy | O(1) | O(1) | String | | |
| 127 | [Word Ladder](src/127.word-ladder.py) | Hard | O(M^2\*N) | O(M^2\*N) | BFS | | |
| 128 | [Longest Consecutive Sequence](src/128.longest-consecutive-sequence.py) | Medium | O(N) | O(N) | Array | | |
| 133 | [Clone Graph](src/133.clone-graph.py) | Medium | O(N+M) | O(N) | DFS, BFS, Graph | | |
| 134 | [Gas Station](src/134.gas-station.py) | Medium | O(N) | O(N) | Dynamic Programming, Greedy | | |
| 135 | [Candy](src/135.candy.py) | Hard | O(N) | O(N) | Greedy | | |
| 138 | [Copy List with Random Pointer](src/138.copy-list-with-random-pointer.py) | Medium | O(N) | O(N) | Hash Table, Linked List | | |
| 139 | [Word Break](src/139.word-break.py) | Medium | O(N^2) | O(N) | Dynamic Programming | | |
| 141 | [Linked List Cycle](src/141.linked-list-cycle.py) | Easy | O(N) | O(1) | Linked List, Two Pointers | | |
| 142 | [Linked List Cycle II](src/142.linked-list-cycle-ii.py) | Medium | O(N) | O(1) | Linked List, Two Pointers | | |
| 143 | [Reorder List](src/143.reorder-list.py) | Medium | O(N) | O(1) | Linked List | | |
| 147 | [Insertion Sort List](src/147.insertion-sort-list.py) | Medium | O(N^2) | O(1) | Sort, Linked List | | |
| 151 | [Evaluate Reverse Polish Notation](src/150.evaluate-reverse-polish-notation.py) | Medium | O(N) | O(N) | Stack | | |
| 151 | [Reverse Words in a String](src/151.reverse-words-in-a-string.py) | Easy | O(N) | O(N) | String | | |
| 152 | [Maximum Product Subarray](src/152.maximum-product-subarray.py) | Medium | O(N) | O(N) | Dynamic Programming, Array | | |
| 153 | [Find Minimum in Rotated Sorted Array](src/153.find-minimum-in-rotated-sorted-array.py) | Medium | O(logN) | O(1) | Binary Search | | |
| 154 | [Find Minimum in Rotated Sorted Array II](src/154.find-minimum-in-rotated-sorted-array-ii.py) | Hard | O(logN) | O(1) | Binary Search | | |
| 159 | [Longest Substring with At Most Two Distinct Characters](src/159.py) | Medium | O(N) | O(1) | Premium, Hash Table, Two Pointers, String, Sliding Window | | |
| 165 | [Compare Version Numbers](src/165.compare-version-numbers.py) | Medium | O(N) | O(1) | String | | |
| 168 | [Excel Sheet Column Title](src/168.excel-sheet-column-title.py) | Medium | O(logN) | O(logN) | Math | Math Tricks | |
| 171 | [Excel Sheet Column Number](src/171.excel-sheet-column-number.py) | Easy | O(N) | O(1) | String | | |
| 179 | [Largest Number](src/179.largest-number.py) | Medium | O(NlogN) | O(1) | Sort | | |
| 187 | [Repeated DNA Sequences](src/187.repeated-dna-sequences.py) | Medium | O(N-L) | O(N-L) | Hash Table, Bit Manipulation | | |
| 190 | [Reverse Bits](src/190.reverse-bits.py) | Easy | O(1) | O(1) | Bit Manipulation | | |
| 198 | [House Robber](src/198.house-robber.py) | Easy | O(N) | O(1) | Dynamic Programming | | |
| 204 | [Count Primes](src/204.count-primes.py) | Medium | O(loglogN) | O(N) | Hash Table, Math | | |
| 207 | [Course Schedule](src/207.course-schedule.py) | Medium | O(N + E) | O(N + E) | BFS, DFS, Graph, Topological Sort | | |
| 208 | [Implement Trie (Prefix Tree)](src/208.implement-trie-prefix-tree.py) | Medium | Varying | Varying | Design, Trie | | |
| 209 | [Minimum Size Subarray Sum](src/209.minimum-size-subarray-sum.py) | Medium | O(N) | O(1) | Array, Two Pointers, Binary Search | | |
| 211 | [Add and Search Word - Data structure design](src/211.add-and-search-word-data-structure-design.py) | Medium | O(M) | O(1) | Trie, Design | | |
| 213 | [House Robber II](src/213.house-robber-ii.py) | Medium | O(N) | O(1) | Dynamic Programming | | |
| 215 | [Kth Largest Element in an Array](src/215.kth-largest-element-in-an-array.py) | Medium | O(NlogK) | O(K) | Heap | | |
| 216 | [Combination Sum III](src/216.combination-sum-iii.py) | Medium | O(N^2) | O(N^2) | Array, Backtracking | | |
| 218 | [The Skyline Problem](src/218.the-skyline-problem.py) | Hard | O(NlogN) | O(N) | Divide and Conquer, Heap, Binary Indexed Tree, Segment Tree, Line Sweep | | |
| 220 | [Contains Duplicate III](src/220.contains-duplicate-iii.py) | Medium | O(N) | O(N) | Sort, Ordered Map | | |
| 221 | [Maximal Square](src/221.maximal-square.py) | Medium | O(N * M) | O(1) | Array, Dynamic Programming | | |
| 222 | [Count Complete Tree Nodes](src/222.count-complete-tree-nodes.py) | Medium | O(logN * logN) | O(1) | Binary Search, Tree | | |
| 227 | [Basic Calculator II](src/227.basic-calculator-ii.py) | Medium | O(N) | O(N) | String, Stack | |
| 228 | [Summary Ranges](src/228.summary-ranges.py) | Easy | O(N) | O(1) | Array | |
| 229 | [Majority Element II](src/229.majority-element-ii.py) | Medium | O(N) | O(1) | Array | |
| 230 | [Kth Smallest Element in a BST](src/230.kth-smallest-element-in-a-bst.py) | Medium | O(H + k) | O(H + k) | Tree, DFS | Use general formula for tree traversal | |
| 231 | [Power of Two](src/231.power-of-two.py) | Easy | O(1) | O(1) | Bit Manipulation | Important technique in bit manipulation | |
| 234 | [Palindrome Linked List](src/234.palindrome-linked-list.py) | Easy | O(N) | O(1) | Linked List, Two Pointers | | |
| 239 | [Sliding Window Maximum](src/239.sliding-window-maximum.py) | Hard | O(N) | O(N) | Monotonic Dequeue, Sliding Window, Heap | | |
| 252 | [Meeting Rooms](src/252.py) | Easy | O(NlogN) | O(1) | Premium, Sort | | 🔒 |
| 253 | [Meeting Rooms II](src/253.py) | Medium | O(NlogN) | O(N) | Premium, Heap, Greedy, Sort | | 🔒 |
| 264 | [Ugly Number II](src/264.ugly-number-ii.py) | Medium | O(1) | O(1) | Heap, Dynamic Programming | | |
| 268 | [Missing Number](src/268.missing-number.py) | Easy | O(N) | O(1) | Array, Math, Bit Manipulation  | | |
| 270 | [Closest Binary Search Tree Value](src/270.py) | Easy | O(H) | O(1) | Premium, Binary Search, Tree | | 🔒 |
| 273 | [Integer to English Words](src/273.integer-to-english-words.py) | Medium | O(logN) | O(1) | Math, String |  | |
| 274 | [H-Index](src/274.h-index.py) | Medium | O(NlogN) | O(N) | Hash Table, Sort | There is a better solution | |
| 283 | [Move Zeroes](src/283.move-zeroes.py) | Easy | O(N) | O(1) | Array, Two Pointers | | |
| 284 | [Peeking Iterator](src/284.peeking-iterator.py) | Medium | O(NlogN) | O(N) | Design | | |
| 289 | [Game of Life](src/289.game-of-life.py) | Medium | O(M*N) | O(1) | Array | | |
| 290 | [Word Pattern](src/290.word-pattern.py) | Easy | O(N) | O(N) | Hash Table | | |
| 295 | [Find Median from Data Stream](src/295.find-median-from-data-stream.py) | Hard | O(logN) | O(N) | Design, Hard, Heap | | |
| 296 | [Best Meeting Point](src/296.py) | Hard | O(M*N) | O(M+N) | Premium, Math | | 🔒 |
| 297 | [Serialize and Deserialize Binary Tree](src/297.serialize-and-deserialize-binary-tree.py) | Hard | O(N) | O(N) | Tree, Design | | |
| 299 | [Bulls and Cows](src/299.bulls-and-cows.py) | Easy | O(N) | O(N) | Hash Table | | |
| 300 | [Longest Increasing Subsequence](src/300.longest-increasing-subsequence.py) | Medium | O(NlogN) | O(N) | Binary Search, Dynamic Programming | | |
| 304 | [Range Sum Query 2D - Immutable](src/304.range-sum-query-2-d-immutable.py) | Medium | O(1) | O(R*C) | Dynamic Programming | Matrix Range Sum Trick | |
| 310 | [Minimum Height Trees](src/310.minimum-height-trees.py) | Medium | O(V) | O(V) | BFS, Graph | | |
| 316 | [Remove Duplicate Letters](src/316.remove-duplicate-letters.py) | Hard | O(N) | O(1) | Greedy, Tricky, Stack | | |
| 317 | [Shortest Distance from All Buildings](src/317.py) | Hard | O(N\*M) | O(N\*M) | BFS, Premium | | 🔒 |
| 319 | [Bulb Switcher](src/319.bulb-switcher.py) | Medium | O(1) | O(1) | Math, Tricky | | |
| 320 | [Generalized Abbreviation](src/320.py) | Medium | O(N*2^N) | O(N) | Premium, Backtracking | | 🔒 |
| 322 | [Coin Change](src/322.coin-change.py) | Medium | O(A*N) | O(A) | Dynamic Programming | | |
| 328 | [Odd Even Linked List](src/328.odd-even-linked-list.py) | Medium | O(N) | O(1) | Linked List | | |
| 329 | [Longest Increasing Path in a Matrix](src/329.longest-increasing-path-in-a-matrix.py) | Hard | O(R\*C) | O(R\*C) | DFS, Topology Sort, Memoization | | |
| 334 | [Increasing Triplet Subsequence](src/334.increasing-triplet-subsequence.py) | Medium | O(N) | O(1) | Array | | |
| 337 | [House Robber III](src/337.house-robber-iii.py) | Medium | O(N) | O(N) | Dynamic Programming, Tree, DFS | | |
| 338 | [Counting Bits](src/338.counting-bits.py) | Medium | O(N) | O(N) | Dynamic Programming, Bit Manipulation | | |
| 342 | [Power of Four](src/342.power-of-four.py) | Easy | O(1) | O(1) | Math, Bit Manipulation | | |
| 344 | [Reverse String](src/344.reverse-string.py) | Easy | O(N) | O(1) | Two Pointers, String | | |
| 346 | [Moving Average from Data Stream](src/346.py) | Easy | O(1) | O(N) | Premium, Design | | 🔒 |
| 347 | [Top K Frequent Elements](src/347.top-k-frequent-elements.py) | Medium | O(N) | O(N) | Hash Table, Heap | | |
| 348 | [Design Tic-Tac-Toe](src/348.py) | Medium | O(1) | O(N^2) | Premium, Design | | 🔒 |
| 351 | [Android Unlock Patterns](src/351.py) | Medium | O(N!) | O(N) | Dynamic Programming, Backtracking, Premium | | 🔒 |
| 354 | [Russian Doll Envelopes](src/354.russian-doll-envelopes.py) | Hard | O(NlogN) | O(N) | Binary Search, Dynamic Programming | | |
| 357 | [Count Numbers with Unique Digits](src/357.count-numbers-with-unique-digits.py) | Medium | O(1) | O(1) | Math, Dynamic Programming, Backtracking | | |
| 361 | [Bomb Enemy](src/361.py) | Medium | O(N\*M) | O(N\*M) | Premium, Dynamic Programming | | 🔒 |
| 362 | [Design Hit Counter](src/362.py) | Medium | O(1) | O(N) | Design, Premium | | 🔒 |
| 363 | [Max Sum of Rectangle No Larger Than K](src/363.max-sum-of-rectangle-no-larger-than-k.py) | Hard | O(R\*R\*C\*logC) | O(R\*C) | Array, Binary Search, Dynamic Programming, Matrix, Ordered Set | | |
| 367 | [Valid Perfect Square](src/367.valid-perfect-square.py) | Easy | O(logN) | O(1) | Math, Binary Search | | |
| 376 | [Wiggle Subsequence](src/376.wiggle-subsequence.py) | Medium | O(N) | O(1) | Greedy, Dynamic Programming | | |
| 377 | [Combination Sum IV](src/377.combination-sum-iv.py) | Medium | O(T*N) | O(T) | Dynamic Programming | | |
| 378 | [Kth Smallest Element in a Sorted Matrix](src/378.kth-smallest-element-in-a-sorted-matrix.py) | Medium | O(N^2logK) | O(K) | Heap, Binary Search | | |
| 380 | [Insert Delete GetRandom](src/380.insert-delete-get-random-o-1.py) | Medium | O(1) | O(N) | Array, Hash Table, Design | | |
| 384 | [Shuffle an Array](src/384.shuffle-an-array.py) | Medium | O(N) | O(N) | | | |
| 387 | [First Unique Character in a String](src/387.first-unique-character-in-a-string.py) | Easy | O(N) | O(N) | | | |
| 389 | [Find the Difference](src/389.find-the-difference.py) | Medium | O(N) | O(1) | Hash Table, Bit Manipulation | | |
| 394 | [Decode String](src/394.decode-string.py) | Medium | O(maxK*N) | O(N) | Stack, DFS | | |
| 395 | [Longest Substring with At Least K Repeating Characters](src/395.longest-substring-with-at-least-k-repeating-characters.py) | Medium | O(NlogN) | O(N) | Divide and Conquer, Recursion, Sliding Window | | |
| 399 | [Evaluate Division](src/399.evaluate-division.py) | Medium | O(N*M) | O(N) | Union Find, Graph | | |
| 402 | [Remove K Digits](src/402.remove-k-digits.py) | Medium | O(N) | O(N) | Greedy | | |
| 404 | [Sum of Left Leaves](src/404.sum-of-left-leaves.py) | Easy | O(N) | O(H) | Tree | | |
| 406 | [Queue Reconstruction by Height](src/406.queue-reconstruction-by-height.py) | Medium | O(N^2) | O(N) | Greedy | Clever solution | |
| 413 | [Arithmetic Slices](src/413.arithmetic-slices.py) | Medium | O(N) | O(1) | Math, Dynamic Programming | | |
| 416 | [Partition Equal Subset Sum](src/416.partition-equal-subset-sum.py) | Medium | O(M*N) | O(M) | Dynamic Programming | | |
| 417 | [Pacific Atlantic Water Flow](src/417.pacific-atlantic-water-flow.py) | Medium | O(R\*C) | O(R\*C) | DFS, BFS | | |
| 419 | [Battleships in a Board](src/419.battleships-in-a-board.py) | Medium | O(N*N) | O(1) | Array, DFS | | |
| 423 | [Reconstruct Original Digits from English](src/423.reconstruct-original-digits-from-english.py) | Medium | O(N) | O(N) | Math | | |
| 425 | [Word Squares](src/425.py) | Hard | Complex | Complex | Back Tracking, Trie, Premium | | 🔒 |
| 428 | [Serialize and Deserialize N-ary Tree](src/428.py) | Hard | O(N) | O(H) | Tree, Premium | | 🔒 |
| 431 | [Encode N-ary Tree to Binary Tree](src/431.py) | Hard | O(N) | O(H) | Tree, Premium | | 🔒 |
| 435 | [Non-overlapping Intervals](src/435.non-overlapping-intervals.py) | Medium | O(NlogN) | O(1) | Greedy | Tricky, Hard | |
| 436 | [Find Right Interval](src/436.find-right-interval.py) | Medium | O(NlogN) | O(N) | Binary Search | Bad Description | |
| 437 | [Path Sum III](src/437.path-sum-iii.py) | Medium | O(N) | O(N) | Tree | Tricky, Hard | |
| 438 | [Find All Anagrams in a String](src/438.find-all-anagrams-in-a-string.py) | Medium | O(N_s + N_p) | O(1) | Hash Table | | |
| 442 | [Find All Duplicates in an Array](src/442.find-all-duplicates-in-an-array.py) | Medium | O(N) | O(1) | Array | | |
| 445 | [Add Two Numbers II](src/445.add-two-numbers-ii.py) | Medium | O(N) | O(N) | Linked List | | |
| 449 | [Serialize and Deserialize BST](src/449.serialize-and-deserialize-bst.py) | Medium | O(N) | O(N) | Tree | | |
| 450 | [Delete Node in a BST](src/450.delete-node-in-a-bst.py) | Medium | O(H) | O(H) | Binary Search Tree | | |
| 451 | [Sort Characters By Frequency](src/451.sort-characters-by-frequency.py) | Medium | O(N) | O(N) | Hash Table, Sorting, Pythonic | | |
| 452 | [Minimum Number of Arrows to Burst Balloons](src/452.minimum-number-of-arrows-to-burst-balloons.py) | Medium | O(NlogN) | O(1) | Sort, Greedy | | |
| 454 | [4Sum II](src/454.4-sum-ii.py) | Medium | O(N^2) | O(N^2) | Array | | |
| 456 | [132 Pattern](src/456.132-pattern.py) | Medium | O(N) | O(N) | Stack | | |
| 458 | [Poor Pigs](src/458.poor-pigs.py) | Hard | O(1) | O(1) | Math | | |
| 462 | [Minimum Moves to Equal Array Elements II](src/462.minimum-moves-to-equal-array-elements-ii.py) | Median | O(NlogN) | O(N) | Math | | |
| 463 | [Island Perimeter](src/463.island-perimeter.py) | Easy | O(N*M) | O(1) | Greedy | | |
| 470 | [Implement Rand10() Using Rand7()](src/470.implement-rand-10-using-rand-7.py) | Medium | O(1) | O(1) | Math | | |
| 473 | [Matchsticks to Square](src/473.matchsticks-to-square.py) | Medium | O(4^N) | O(4^N) | DFS, Dynamic Programming | | |
| 474 | [Ones and Zeroes](src/474.ones-and-zeroes.py) | Medium | O(K\*M\*N) | O(K\*M\*N) | Dynamic Programming | | |
| 476 | [Number Complement](src/476.number-complement.py) | Easy | O(N) | O(1) | Bit Manipulation | | |
| 478 | [Generate Random Point in a Circle](src/478.generate-random-point-in-a-circle.py) | Medium | O(1) | O(1) | Math, Random, Rejection Sampling | | |
| 491 | [Increasing Subsequences](src/491.increasing-subsequences.py) | Medium | O(Combination) | O(Combination) | DFS | | |
| 494 | [Target Sum](src/494.target-sum.py) | Medium | O(N\*T) | O(T) | Dynamic Programming, DFS | Template for DP | |
| 495 | [Teemo Attacking](src/495.teemo-attacking.py) | Medium | O(N) | O(1) | Array | | |
| 497 | [Random Point in Non-overlapping Rectangles](src/497.random-point-in-non-overlapping-rectangles.py) | Medium | O(logN) | O(N) | Design, Binary Search | | |
| 498 | [Diagonal Traverse](src/498.diagonal-traverse.py) | Medium | O(R\*C) | O(R\*C) | Array | | |
| 510 | [Inorder Successor in BST II](src/510.py) | Medium | O(H) | O(1) | Tree, Premium | | 🔒 |
| 520 | [Detect Capital](src/520.detect-capital.py) | Easy | O(N) | O(1) | | | |
| 524 | [Longest Word in Dictionary through Deleting](src/524.longest-word-in-dictionary-through-deleting.py) | Medium | Complex | Complex | Two Pointers, Sort | | |
| 525 | [Contiguous Array](src/525.contiguous-array.py) | Medium | O(N) | O(N) | Hash Table | Very good problem | |
| 528 | [Random Pick with Weight](src/528.random-pick-with-weight.py) | Medium | O(N), O(logN) | O(N), O(1) | Binary Search, Random | Pythonic | |
| 532 | [K-diff Pairs in an Array](src/532.k-diff-pairs-in-an-array.py) | Medium | O(N) | O(N) | Array, Two Pointers | | |
| 538 | [Convert BST to Greater Tree](src/538.convert-bst-to-greater-tree.py) | Medium | O(N) | O(H) | Tree, BFS, DFS, Recursion | | |
| 540 | [Single Element in a Sorted Array](src/540.single-element-in-a-sorted-array.py) | Medium | O(logN) | O(1) | Binary Search | | |
| 542 | [01 Matrix](src/542.01-matrix.py) | Medium | O(R\*C) | O(R\*C) | BFS, DFS | | |
| 554 | [Brick Wall](src/554.brick-wall.py) | Medium | O(N) | O(N) | Hash Table | | |
| 563 | [Binary Tree Tilt](src/563.binary-tree-tilt.py) | Easy | O(N) | O(H) | Tree, DFS, Recursion | | |
| 567 | [Permutation in String](src/567.permutation-in-string.py) | Medium | O(S1 + S2) | O(1) | String, Two Pointers, Sliding Window | | |
| 573 | [Squirrel Simulation](src/573.py) | Medium | O(N) | O(1) | Premium, Math | | 🔒 |
| 581 | [Shortest Unsorted Continuous Subarray](src/581.shortest-unsorted-continuous-subarray.py) | Medium | O(N) | O(1) | Array | | |
| 583 | [Delete Operation for Two Strings](src/583.delete-operation-for-two-strings.py) | Medium | O(N^2) | O(N) | Dynamic Programming, String | | |
| 589 | [N-ary Tree Preorder Traversal](src/589.n-ary-tree-preorder-traversal.py) | Easy | O(N) | O(N) | Tree | | |
| 593 | [Valid Square](src/593.valid-square.py) | Medium | O(1) | O(1) | Math | | |
| 605 | [Can Place Flowers](src/605.can-place-flowers.py) | Easy | O(N) | O(1) | Array, Greedy | | |
| 611 | [Valid Triangle Number](src/611.valid-triangle-number.py) | Medium | O(N^2) | O(1) | Array, Two Pointers, Binary Search, Greedy, Sorting | | |
| 622 | [Design Circular Queue](src/622.design-circular-queue.py) | Medium | O(1) | O(1) | Design, Queue | | |
| 623 | [Add One Row to Tree](src/623.add-one-row-to-tree.py) | Medium | O(N) | O(N) | Tree | | |
| 624 | [Maximum Distance in Arrays](src/624.py) | Easy | O(N) | O(1) | Hash Table, Array, Premium | | 🔒 |
| 639 | [Decode Ways II](src/639.decode-ways-ii.py) | Hard | O(N) | O(N) | String, Dynamic Programming | | |
| 646 | [Maximum Length of Pair Chain](src/646.maximum-length-of-pair-chain.py) | Medium | O(NlogN) | O(N) | Greedy, Dynamic Programming | | |
| 655 | [Print Binary Tree](src/655.print-binary-tree.py) | Medium | O(N) | O(H) | Tree | | |
| 658 | [Find K Closest Elements](src/658.find-k-closest-elements.py) | Medium | O(logN+K) | O(K) | Tree | | |
| 659 | [Split Array into Consecutive Subsequences](src/659.split-array-into-consecutive-subsequences.py) | Medium | O(N) | O(1) | Greedy | | |
| 662 | [Maximum Width of Binary Tree](src/662.maximum-width-of-binary-tree.py) | Medium | O(N) | O(N) | Tree | | |
| 665 | [Non-decreasing Array](src/665.non-decreasing-array.py) | Medium | O(N) | O(1) | Array | | |
| 667 | [Beautiful Arrangement II](src/667.beautiful-arrangement-ii.py) | Medium | O(N) | O(N) | Array | | |
| 669 | [Trim a Binary Search Tree](src/669.trim-a-binary-search-tree.py) | Medium | O(N) | O(N) | Tree, Recursion | | |
| 670 | [Maximum Swap](src/670.maximum-swap.py) | Medium | O(N) | O(N) | Array, Math | | |
| 673 | [Number of Longest Increasing Subsequence](src/673.number-of-longest-increasing-subsequence.py) | Medium | O(N^2) | O(N) | Dynamic Programming | | |
| 677 | [Map Sum Pairs](src/677.map-sum-pairs.py) | Medium | O(K) | O(K) | Trie | | |
| 696 | [Count Binary Substrings](src/696.count-binary-substrings.py) | Medium | O(N) | O(1) | String | | |
| 700 | [Search in a Binary Search Tree](src/700.search-in-a-binary-search-tree.py) | Easy | O(H) | O(1) | Tree | | |
| 701 | [Insert into a Binary Search Tree](src/701.insert-into-a-binary-search-tree.py) | Medium | O(H) | O(1) | Tree | | |
| 702 | [Search in a Sorted Array of Unknown Size](src/702.py) | Medium | O(logN) | O(1) | Binary Search, Premium | | 🔒 |
| 705 | [Design HashSet](src/705.design-hash-set.py) | Easy | Varying | Varying | Design HashSet | | |
| 708 | [Insert into a Sorted Circular Linked List](src/708.py) | Medium | O(N) | O(1) | Linked List, Premium | | 🔒 |
| 713 | [Subarray Product Less Than K](src/713.subarray-product-less-than-k.py) | Medium | O(N) | O(1) | Array, Two Pointers | | |
| 714 | [Best Time to Buy and Sell Stock with Transaction Fee](src/714.best-time-to-buy-and-sell-stock-with-transaction-fee.py) | Medium | O(N) | O(1) | Array, Dynamic Programming, Greedy | | |
| 721 | [Accounts Merge](src/721.accounts-merge.py) | Medium | Complex | Complex | Union-Find, DFS | Template for Union-Find | |
| 725 | [Split Linked List in Parts](src/725.split-linked-list-in-parts.py) | Medium | O(N) | O(N) | Linked List | | |
| 729 | [My Calendar I](src/729.my-calendar-i.py) | Medium | O(NlogN) | O(N) | Tree | | |
| 733 | [Flood Fill](src/733.flood-fill.py) | Easy | O(N) | O(N) | DFS | | |
| 734 | [Sentence Similarity](src/734.py) | Easy | O(N) | O(N) | Premium, Hash Table | | 🔒 |
| 735 | [Asteroid Collision](src/735.asteroid-collision.py) | Medium | O(N) | O(N) | Stack | | |
| 737 | [Sentence Similarity II](src/737.py) | Medium | O(NlogP + P) or o(NP) | O(N) | Premium, DFS, Union Find | | 🔒 |
| 738 | [Monotone Increasing Digits](src/738.monotone-increasing-digits.py) | Medium | O(logN) | O(logN) | Greedy | | |
| 739 | [Daily Temperatures](src/739.daily-temperatures.py) | Medium | O(N) | O(N) | Hash Table, Stack | | |
| 740 | [Delete and Earn](src/740.delete-and-earn.py) | Medium | O(N+M) | O(N+M) | Dynamic Programming | | |
| 743 | [Network Delay Time](src/743.network-delay-time.py) | Medium | O(ElogE) | O(N + E) | Heap, BFS, DFS, Graph | | |
| 752 | [Open the Lock](src/752.open-the-lock.py) | Medium | O(N^2\*D^N) | O(N^2\*D^N) | BFS | | |
| 754 | [Reach a Number](src/754.reach-a-number.py) | Medium | O(logN) | O(1) | Math | | |
| 763 | [Partition Labels](src/763.partition-labels.py) | Medium | O(N) | O(N) | Greedy, Two Pointers | | |
| 767 | [Reorganize String](src/767.reorganize-string.py) | Medium | O(NlogN) | O(N) |  String, Heap, Greedy, Sort | | |
| 768 | [Max Chunks To Make Sorted II](src/768.max-chunks-to-make-sorted-ii.py) | Hard | O(N) | O(N) | Array | | |
| 769 | [Max Chunks To Make Sorted](src/769.max-chunks-to-make-sorted.py) | Medium | O(N) | O(1) | Array | | |
| 775 | [Global and Local Inversions](src/775.global-and-local-inversions.py) | Medium | O(N) | O(1) | Array, Math | | |
| 778 | [Swim in Rising Water](src/778.swim-in-rising-water.py) | Medium | O(R\*C\*logN) | O(R\*C) | Binary Search, Heap, DFS, Union Find | | |
| 784 | [Letter Case Permutation](src/784.letter-case-permutation.py) | Medium | O(2^N) | O(2^N) | Backtracking, Bit Manipulation | | |
| 785 | [Is Graph Bipartite?](src/785.is-graph-bipartite.py) | Medium | O(E+V) | O(E+V) | BFS, DFS, Graph | | |
| 787 | [Cheapest Flights Within K Stops](src/787.cheapest-flights-within-k-stops.py) | Medium | Complex | Complex | Dijkstra's Algorithm, Graph | Quite hard | |
| 789 | [Escape The Ghosts](src/789.escape-the-ghosts.py) | Medium | O(N) | O(1) | Math | | |
| 791 | [Custom Sort String](src/791.custom-sort-string.py) | Medium | O(N) | O(N) | String | | |
| 792 | [Number of Matching Subsequences](src/792.number-of-matching-subsequences.py) | Medium | O(N + M * L) | O(M) | Array | | |
| 794 | [Valid Tic-Tac-Toe State](src/794.valid-tic-tac-toe-state.py) | Medium | O(1) | O(1) | Array, String | | |
| 795 | [Number of Subarrays with Bounded Maximum](src/795.number-of-subarrays-with-bounded-maximum.py) | Medium | O(N) | O(1) | Array | | |
| 797 | [All Paths From Source to Target](src/797.all-paths-from-source-to-target.py) | Medium | O(2^N * N) | O(2^N * N) | Backtracking, DFS | | |
| 799 | [Champagne Tower](src/799.champagne-tower.py) | Medium | O(R^2) | O(R^2) | Dynamic Programming | | |
| 802 | [Find Eventual Safe States](src/802.find-eventual-safe-states.py) | Medium | O(V+E) | O(V+E) | DFS, Graph | | |
| 820 | [Short Encoding of Words](src/820.short-encoding-of-words.py) | Medium | O(N\*M) | O(N\*M) | Trie | | |
| 823 | [Binary Trees With Factors](src/823.binary-trees-with-factors.py) | Medium | O(N*N) | O(N) | Dynamic Programming | | |
| 825 | [Friends Of Appropriate Ages](src/825.friends-of-appropriate-ages.py) | Medium | O(N) | O(1) | Array | | |
| 830 | [Positions of Large Groups](src/830.positions-of-large-groups.py) | Easy | O(N) | O(1) | | | |
| 833 | [Find And Replace in String](src/833.find-and-replace-in-string.py) | Medium | O(N) | O(N) | Dynamic Programming | | |
| 835 | [Image Overlap](src/835.image-overlap.py) | Medium | O(N^2) | O(N) | | | |
| 838 | [Push Dominoes](src/838.push-dominoes.py) | Medium | O(N) | O(N) | | | |
| 841 | [Keys and Rooms](src/841.keys-and-rooms.py) | Medium | O(N^2) | O(N) | DFS, Graph | | |
| 845 | [Longest Mountain in Array](src/845.longest-mountain-in-array.py) | Medium | O(N) | O(1) | Two Pointers | | |
| 846 | [Hand of Straights](src/846.hand-of-straights.py) | Medium | O(MlogM+NW) | O(N) | Ordered Map | | |
| 849 | [Maximize Distance to Closest Person](src/849.maximize-distance-to-closest-person.py) | Medium | O(N) | O(1) | Array | | |
| 851 | [Loud and Rich](src/851.loud-and-rich.py) | Medium | O(N^2) | O(N^2) | DFS | | |
| 853 | [Car Fleet](src/853.car-fleet.py) | Medium | O(NlogN) | O(N) | Sort | | |
| 858 | [Mirror Reflection](src/858.mirror-reflection.py) | Medium | O(logN) | O(1) | Math | | |
| 859 | [Buddy Strings](src/859.buddy-strings.py) | Easy | O(N) | O(1) | String | | |
| 863 | [All Nodes Distance K in Binary Tree](src/863.all-nodes-distance-k-in-binary-tree.py) | Medium | O(N) | O(N) | Tree, BFS, DFS | | |
| 865 | [Smallest Subtree with all the Deepest Nodes](src/865.smallest-subtree-with-all-the-deepest-nodes.py) | Medium | O(N) | O(N) | Tree, BFS, DFS, Recursion | | |
| 869 | [Reordered Power of 2](src/869.reordered-power-of-2.py) | Medium | O(logN) | O(1) | Math | | |
| 870 | [Advantage Shuffle](src/870.advantage-shuffle.py) | Medium | O(NlogN) | O(N) | Array, Greedy | | |
| 873 | [Length of Longest Fibonacci Subsequence](src/873.length-of-longest-fibonacci-subsequence.py) | Medium | O(N^2) | O(N^2) | Array, Dynamic Programming | | |
| 875 | [Koko Eating Bananas](src/875.koko-eating-bananas.py) | Medium | O(NlogN) | O(1) | Binary Search | | |
| 880 | [Decoded String at Index](src/880.decoded-string-at-index.py) | Medium | O(N) | O(1) | Stack | Good problem | |
| 881 | [Boats to Save People](src/881.boats-to-save-people.py) | Medium | O(NlogN) | O(N) | Two Pointers, Greedy | | |
| 886 | [Possible Bipartition](src/886.possible-bipartition.py) | Medium | O(N + E) | O(N + E) | DFS | Good problem | |
| 890 | [Find and Replace Pattern](src/890.find-and-replace-pattern.py) | Medium | O(N\*K) | O(N\*K) | String | | |
| 892 | [Surface Area of 3D Shapes](src/892.surface-area-of-3-d-shapes.py) | Easy | O(N*N) | O(1) | Math, Geometry | | |
| 895 | [Maximum Frequency Stack](src/895.maximum-frequency-stack.py) | Medium | O(1) | O(N) | Hash Table, Stack | | |
| 901 | [Online Stock Span](src/901.online-stock-span.py) | Medium | O(1) | O(N) | Monotonic Stack | | |
| 902 | [Numbers At Most N Given Digit Set](src/902.numbers-at-most-n-given-digit-set.py) | Hard | O(LogN) | O(1) | Math, Dynamic Programming | | |
| 904 | [Fruit Into Baskets](src/904.fruit-into-baskets.py) | Medium | O(N) | O(1) | Two Pointers | | |
| 905 | [Sort Array By Parity](src/905.sort-array-by-parity.py) | Easy | O(N) | O(1) | Array | | |
| 906 | [Super Palindromes](src/906.super-palindromes.py) | Hard | Complex | Complex | Math | | |
| 910 | [Smallest Range II](src/910.smallest-range-ii.py) | Medium | O(NlogN) | O(N) | Math, Greedy | | |
| 911 | [Online Election](src/911.online-election.py) | Medium | O(N + QlogN) | O(N) | Binary Search | | |
| 915 | [Partition Array into Disjoint Intervals](src/915.partition-array-into-disjoint-intervals.py) | Medium | O(N) | O(N) | Array | | |
| 916 | [Word Subsets](src/916.word-subsets.py) | Medium | O(A_t + B_t) | O(L) | String | | |
| 918 | [Maximum Sum Circular Subarray](src/918.maximum-sum-circular-subarray.py) | Medium | O(N) | O(1) | Array, Dynamic Programming | | |
| 919 | [Complete Binary Tree Inserter](src/919.complete-binary-tree-inserter.py) | Medium | O(N) | O(1) | Tree | | |
| 923 | [3Sum With Multiplicity](src/923.3-sum-with-multiplicity.py) | Medium | O(N^2) | O(N) | Two Pointers | | |
| 926 | [Flip String to Monotone Increasing](src/926.flip-string-to-monotone-increasing.py) | Medium | O(N) | O(N) | Array | | |
| 930 | [Binary Subarrays With Sum](src/930.binary-subarrays-with-sum.py) | Medium | O(N) | O(N) | Hash Table, Two Pointers | | |
| 933 | [Number of Recent Calls](src/933.number-of-recent-calls.py) | Easy | O(1) | O(1) | Queue | | |
| 934 | [Shortest Bridge](src/934.shortest-bridge.py) | Medium | O(E+V) | O(E+V) | BFS, DFS | | |
| 935 | [Knight Dialer](src/935.knight-dialer.py) | Medium | O(N) | O(1) | Dynamic Programming | | |
| 941 | [Valid Mountain Array](src/941.valid-mountain-array.py) | Easy | O(N) | O(1) | Array | | |
| 946 | [Validate Stack Sequences](src/946.validate-stack-sequences.py) | Medium | O(N) | O(N) | Stack | | |
| 948 | [Bag of Tokens](src/948.bag-of-tokens.py) | Medium | O(NlogN) | O(N) | Greedy | | |
| 953 | [Verifying an Alien Dictionary](src/953.verifying-an-alien-dictionary.py) | Easy | O(A) | O(1) | Hash Table | | |
| 957 | [Prison Cells After N Days](src/957.prison-cells-after-n-days.py) | Medium | O(1) | O(1) | Hash Table | | |
| 958 | [Check Completeness of a Binary Tree](src/958.check-completeness-of-a-binary-tree.py) | Medium | O(N) | O(N) | Tree | | |
| 962 | [Maximum Width Ramp](src/962.maximum-width-ramp.py) | Medium | O(NlogN) | O(N) | Array | | |
| 966 | [Vowel Spellchecker](src/966.vowel-spellchecker.py) | Medium | O(N) | O(N) | Hash Table, String | | |
| 967 | [Numbers With Same Consecutive Differences](src/967.numbers-with-same-consecutive-differences.py) | Medium | O(N*2^N) | O(2^N) | DFS | | |
| 968 | [Binary Tree Cameras](src/968.binary-tree-cameras.py) | Hard | O(N) | O(H) | Greedy, Tree, Dynamic Programming, DFS | New Technique | |
| 969 | [Pancake Sorting](src/969.pancake-sorting.py) | Medium | O(N^2) | O(N) | Array | | |
| 970 | [Powerful Integers](src/970.powerful-integers.py) | Medium | O(logx*logy) | O(logx+logy) | Hash Table, Math | | |
| 971 | [Flip Binary Tree To Match Preorder Traversal](src/971.flip-binary-tree-to-match-preorder-traversal.py) | Medium | O(N) | O(N) | Tree, DFS | | |
| 973 | [K Closest Points to Origin](src/973.k-closest-points-to-origin.py) | Medium | O(N log(K)) | O(K) | Divide and Conquer, Heap, Sort | | |
| 974 | [Subarray Sums Divisible by K](src/974.subarray-sums-divisible-by-k.py) | Medium | O(N) | O(K) | Array, Hash Table | | |
| 976 | [Largest Perimeter Triangle](src/976.largest-perimeter-triangle.py) | Medium | O(NlogN) | O(N) | Math, Sort | | |
| 977 | [Squares of a Sorted Array](src/977.squares-of-a-sorted-array.py) | Easy | O(N) | O(N) | Array, Two Pointers | | |
| 979 | [Distribute Coins in Binary Tree](src/979.distribute-coins-in-binary-tree.py) | Medium | O(N) | O(H) | Tree, DFS | | |
| 980 | [Unique Paths III](src/980.unique-paths-iii.py) | Medium | O(2^N) | O(N) | Backtracking, DFS | | |
| 983 | [Minimum Cost For Tickets](src/983.minimum-cost-for-tickets.py) | Medium | O(365) | O(365) | LRU Cache, Dynamic Programming | | |
| 986 | [Interval List Intersections](src/986.interval-list-intersections.py) | Medium | O(N + M) | O(1) | Two Pointers | | |
| 987 | [Vertical Order Traversal of a Binary Tree](src/987.vertical-order-traversal-of-a-binary-tree.py) | Medium | O(NlogN) | O(N) | Hash Table, Tree | | |
| 991 | [Broken Calculator](src/991.broken-calculator.py) | Medium | O(logN) | O(1) | Math, Greedy | | |
| 992 | [Subarrays with K Different Integers](src/992.subarrays-with-k-different-integers.py) | Hard | O(N) | O(N) | Hash Talble, Two Pointers, Sliding Window | | |
| 993 | [Cousins in Binary Tree](src/993.cousins-in-binary-tree.py) | Easy | O(N) | O(H) | Trees, Recursion | | |
| 994 | [Rotting Oranges](src/994.rotting-oranges.py) | Medium | O(N^2) | O(N) | Trees, Recursion | | |
| 1003 | [Check If Word Is Valid After Substitutions](src/1003.check-if-word-is-valid-after-substitutions.py) | Medium | O(N) | O(N) | String, Stack | | |
| 1004 | [Max Consecutive Ones III](src/1004.max-consecutive-ones-iii.py) | Medium | O(N) | O(1) | Sliding Window, Two Pointers | | |
| 1007 | [Minimum Domino Rotations For Equal Row](src/1007.minimum-domino-rotations-for-equal-row.py) | Medium | O(N) | O(1) | Array, Greedy | | |
| 1010 | [Pairs of Songs With Total Durations Divisible by 60](src/1010.pairs-of-songs-with-total-durations-divisible-by-60.py) | Medium | O(N) | O(1) | Array, Math | | |
| 1011 | [Capacity To Ship Packages Within D Days](src/1011.capacity-to-ship-packages-within-d-days.py) | Medium | O(NlogN) | O(1) | Array, Binary Search | | |
| 1014 | [Best Sightseeing Pair](src/1014.best-sightseeing-pair.py) | Medium | O(N) | O(1) | Array | | |
| 1015 | [Smallest Integer Divisible by K](src/1015.smallest-integer-divisible-by-k.py) | Medium | O(K) | O(K) | Math | | |
| 1022 | [Sum of Root To Leaf Binary Numbers](src/1022.sum-of-root-to-leaf-binary-numbers.py) | Easy | O(N) | O(H) | Tree | | |
| 1023 | [Camelcase Matching](src/1023.camelcase-matching.py) | Medium | O(Q*N) | O(Q) | String, Trie | | |
| 1024 | [Video Stitching](src/1024.video-stitching.py) | Medium | O(NlogN) | O(1) | Dynamic Programming | | |
| 1026 | [Maximum Difference Between Node and Ancestor](src/1026.maximum-difference-between-node-and-ancestor.py) | Medium | O(N) | O(H) | Tree, DFS | | |
| 1029 | [Two City Scheduling](src/1029.two-city-scheduling.py) | Easy | O(NlogN) | O(N) | Greedy | Good Problem | |
| 1032 | [Stream of Characters](src/1032.stream-of-characters.py) | Hard | O(M) | O(M) | Trie | | |
| 1035 | [Uncrossed Lines](src/1035.uncrossed-lines.py) | Medium | O(N^2) | O(N) | Array, Dynamic Programming | | |
| 1042 | [Flower Planting With No Adjacent](src/1042.flower-planting-with-no-adjacent.py) | Medium | O(V+E) | O(V+E) | Graph | | |
| 1048 | [Longest String Chain](src/1048.longest-string-chain.py) | Medium | `O(N*logN+N*C*C)` | `O(N)` | Hash Table, Dynamic Programming | | |
| 1052 | [Grumpy Bookstore Owner](src/1052.grumpy-bookstore-owner.py) | Medium | O(N) | O(N) | Sliding Window, Array | | |
| 1053 | [Previous Permutation With One Swap](src/1053.previous-permutation-with-one-swap.py) | Medium | O(N) | O(N) | Array, Greedy | | |
| 1054 | [Distant Barcodes](src/1054.distant-barcodes.py) | Medium | O(NlogN) | O(N) | Sort, Heap | | |
| 1060 | [Missing Element in Sorted Array](src/1060.missing-element-in-sorted-array.py) | Medium | O(logN) | O(1) | Binary Search, Premium | | 🔒 |
| 1061 | [Lexicographically Smallest Equivalent String](src/1061.py) | Medium | O(N) | O(N) | DFS, Union Find, Premium | | 🔒 |
| 1074 | [Number of Submatrices That Sum to Target](src/1074.number-of-submatrices-that-sum-to-target.py) | Hard | O(R\*R\*C) | O(R\*C) | Array, Dynamic Programming, Sliding Window | | |
| 1080 | [Insufficient Nodes in Root to Leaf Paths](src/1080.insufficient-nodes-in-root-to-leaf-paths.py) | Medium | O(N) | O(N) | DFS | | |
| 1091 | [Shortest Path in Binary Matrix](src/1091.shortest-path-in-binary-matrix.py) | Medium | O(N) | O(N) | BFS | | |
| 1094 | [Car Pooling](src/1094.car-pooling.py) | Medium | O(N) | O(1) | Car Pooling | | |
| 1109 | [Corporate Flight Bookings](src/1109.corporate-flight-bookings.py) | Medium | O(N) | O(N) | Array, Math | | |
| 1130 | [Minimum Cost Tree From Leaf Values](src/1130.minimum-cost-tree-from-leaf-values.py) | Medium | O(N) | O(N) | Dynamic Programming, Tree, Stack | | |
| 1162 | [As Far from Land as Possible](src/1162.as-far-from-land-as-possible.py) | Medium | O(N\*M) | O(N\*M) | Graph, BFS | | |
| 1192 | [Critical Connections in a Network](src/1192.critical-connections-in-a-network.py) | Medium | O(V+E) | O(V+E) | DFS, Tarjan | New Algorithm | |
| 1209 | [Remove All Adjacent Duplicates in String II](src/1209.remove-all-adjacent-duplicates-in-string-ii.py) | Medium | O(N) | O(N) | Stack | | |
| 1217 | [Minimum Cost to Move Chips to The Same Position](src/1217.minimum-cost-to-move-chips-to-the-same-position.py) | Easy | O(N) | O(1) | Math, Greedy, Array | | |
| 1218 | [Longest Arithmetic Subsequence of Given Difference](src/1218.longest-arithmetic-subsequence-of-given-difference.py) | Medium | O(N) | O(N) | Hash Table, Math, Dynamic Programming | | |
| 1219 | [Minimum CostPath with Maximum Gold](src/1219.path-with-maximum-gold.py) | Medium | O(R\*C+N\*2^N) |  O(N) | Backtracking | | |
| 1220 | [Count Vowels Permutation](src/1220.count-vowels-permutation.py) | Hard | O(N) |  O(N) | Dynamic Programming | | |
| 1232 | [Check If It Is a Straight Line](src/1232.check-if-it-is-a-straight-line.py) | Easy | O(N) | O(1) | Math, Pythonic, Geometry | | |
| 1239 | [Maximum Length of a Concatenated String with Unique Characters](src/1239.maximum-length-of-a-concatenated-string-with-unique-characters.py) | Medium | O(2^N) | O(N) | Backtracking, Bit Manipulation | | |
| 1249 | [Minimum Remove to Make Valid Parentheses](src/1249.minimum-remove-to-make-valid-parentheses.py) | Medium | O(N) | O(N) | Stack, String | | |
| 1277 | [Count Square Submatrices with All Ones](src/1277.count-square-submatrices-with-all-ones.py) | Medium | O(N * M) | O(1) | Array, Dynamic Programming | | |
| 1283 | [Find the Smallest Divisor Given a Threshold](src/1283.find-the-smallest-divisor-given-a-threshold.py) | Medium | O(NlogNmax) | O(1) | Binary Search | | |
| 1288 | [Remove Covered Intervals](src/1288.remove-covered-intervals.py) | Medium | O(N) | O(1) | Greedy, Sort, Line Sweep | | |
| 1290 | [Convert Binary Number in a Linked List to Integer](src/1290.convert-binary-number-in-a-linked-list-to-integer.py) | Easy | O(N) | O(1) | Linked List, Bit Manipulation | | |
| 1291 | [Sequential Digits](src/1291.sequential-digits.py) | Medium | O(N) | O(N) | Backtracking | | |
| 1298 | [Maximum Candies You Can Get from Boxes](src/1298.maximum-candies-you-can-get-from-boxes.py) | Medium | O(B+K) | O(B) | BFS | | |
| 1305 | [All Elements in Two Binary Search Trees](src/1305.all-elements-in-two-binary-search-trees.py) | Medium | O(N) | O(N) | Sort, Tree | | |
| 1306 | [All Elements inJump Game III](src/1306.jump-game-iii.py) | Medium | O(N) | O(N) | BFS, DFS, Recursion | | |
| 1315 | [Sum of Nodes with Even-Valued Grandparent](src/1315.sum-of-nodes-with-even-valued-grandparent.py) | Medium | O(N) | O(N) | Tree, DFS | | |
| 1332 | [Remove Palindromic Subsequences](src/1332.remove-palindromic-subsequences.py) | Easy | O(N) | O(1) | String | | |
| 1337 | [The K Weakest Rows in a Matrix](src/1337.the-k-weakest-rows-in-a-matrix.py) | Easy | O(MlogKlogN) | O(K) | Heap, Array, Binary Search | | |
| 1344 | [Angle Between Hands of a Clock](src/1344.angle-between-hands-of-a-clock.py) | Medium | O(1) | O(1) | Math | | |
| 1345 | [Jump Game IV](src/1345.jump-game-iv.py) | Hard | O(N) | O(N) | BFS | | |
| 1354 | [Construct Target Array With Multiple Sums](src/1354.construct-target-array-with-multiple-sums.py) | Hard | O(NlogN) | O(N) | Greedy, Heap | Very Hard | |
| 1371 | [Find the Longest Substring Containing Vowels in Even Counts](src/1371.find-the-longest-substring-containing-vowels-in-even-counts.py) | Medium | O(N) | O(N) | String | | |
| 1375 | [Bulb Switcher III](src/1375.bulb-switcher-iii.py) | Medium | O(N) | O(1) | Array | | |
| 1387 | [Sort Integers by The Power Value](src/1387.sort-integers-by-the-power-value.py) | Medium | O(NlogK) | O(N) | Sort, Graph | | |
| 1395 | [Count Number of Teams](src/1395.count-number-of-teams.py) | Medium | O(N^2) | O(1) | Array | | |
| 1396 | [Design Underground System](src/1396.design-underground-system.py) | Medium | O(N) | O(N) | Design | | |
| 1405 | [Longest Happy String](src/1405.longest-happy-string.py) | Medium | O(N) | O(N) | Greedy, Dynamic Programming | | |
| 1419 | [Minimum Number of Frogs Croaking](src/1419.minimum-number-of-frogs-croaking.py) | Medium | O(N) | O(1) | String | | |
| 1423 | [Maximum Points You Can Obtain from Cards](src/1423.maximum-points-you-can-obtain-from-cards.py) | Medium | O(N) | O(1) | Array, Dynamic Programming, Sliding Window | | |
| 1424 | [Diagonal Traverse II](src/1424.diagonal-traverse-ii.py) | Medium | O(A) | O(A) | Array | | |
| 1426 | [Counting Elements](src/1426.counting-elements.py) | Easy | O(N) | O(N) | Array, Premium | | 🔒 |
| 1427 | [Perform String Shifts](src/1427.perform-string-shifts.py) | Easy | O(N + S) | O(1) | Premium | | 🔒 |
| 1437 | [Check If All 1's Are at Least Length K Places Away](src/1437.check-if-all-1-s-are-at-least-length-k-places-away.py) | Easy | O(N) | O(1) | Array | | |
| 1441 | [Build an Array With Stack Operations](src/1441.build-an-array-with-stack-operations.py) | Easy | O(N) | O(N) | Pythonic | | |
| 1442 | [Count Triplets That Can Form Two Arrays of Equal XOR](src/1442.count-triplets-that-can-form-two-arrays-of-equal-xor.py) | Medium | O(N) | O(N) | Array, Math, Bit Manipulation | | |
| 1443 | [Minimum Time to Collect All Apples in a Tree](src/1443.minimum-time-to-collect-all-apples-in-a-tree.py) | Medium | O(E) | O(E) | Tree, DFS | | |
| 1444 | [Number of Ways of Cutting a Pizza](src/1444.number-of-ways-of-cutting-a-pizza.py) | Hard | O(K\*R\*C\*(R+C)) | O(K\*R\*C) | Dynamic Programming | | |
| 1446 | [Consecutive Characters](src/1446.consecutive-characters.py) | Easy | O(N) | O(1) | String | | |
| 1447 | [Simplified Fractions](src/1447.simplified-fractions.py) | Medium | Varying | Varying | | | |
| 1448 | [Count Good Nodes in Binary Tree](src/1448.count-good-nodes-in-binary-tree.py) | Medium | O(N) | O(H) | Tree, DFS | | |
| 1450 | [Number of Students Doing Homework at a Given Time](src/1450.number-of-students-doing-homework-at-a-given-time.py) | Easy | O(N) | O(1) | | | |
| 1451 | [Rearrange Words in a Sentence](src/1451.rearrange-words-in-a-sentence.py) | Medium | O(N * logN) | O(1) | String, Sort | | |
| 1452 | [People Whose List of Favorite Companies Is Not a Subset of Another List](src/1452.people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list.py) | Medium | O(N^2) | O(N) | String, Sort | There is a better solution | |
| 1455 | [Check If a Word Occurs As a Prefix of Any Word in a Sentence](src/1455.check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence.py) | Medium | O(N) | O(1) | String, Pythonic | | |
| 1456 | [Maximum Number of Vowels in a Substring of Given Length](src/1456.maximum-number-of-vowels-in-a-substring-of-given-length.py) | Medium | O(N) | O(1) | String, Sliding Window | | |
| 1457 | [Pseudo-Palindromic Paths in a Binary Tree](src/1457.pseudo-palindromic-paths-in-a-binary-tree.py) | Medium | O(N) | O(H) | Bit Manipulation, Tree, DFS   | | |
| 1460 | [Make Two Arrays Equal by Reversing Sub-arrays](src/1460.make-two-arrays-equal-by-reversing-sub-arrays.py) | Easy | O(N) | O(1) | Array | | |
| 1461 | [Check If a String Contains All Binary Codes of Size K](src/1461.check-if-a-string-contains-all-binary-codes-of-size-k.py) | Medium | O(N) | O(2**K) | String, Bit Manipulation | | |
| 1463 | [Cherry Pickup II](src/1463.cherry-pickup-ii.py) | hard | O(R\*C\*C) | O(R\*C\*C) | Dynamic Programming | | |
| 1464 | [Maximum Product of Two Elements in an Array](src/1464.maximum-product-of-two-elements-in-an-array.py) | Easy | O(N) | O(1) | Array | | |
| 1465 | [Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts](src/1465.maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts.py) | Medium | O(NlogN) | O(N) | Array | | |
| 1466 | [Reorder Routes to Make All Paths Lead to the City Zero](src/1466.reorder-routes-to-make-all-paths-lead-to-the-city-zero.py) | Medium | O(\|V\|) | O(\|V\|) | Tree, DFS | | |
| 1470 | [Shuffle the Array](src/1470.shuffle-the-array.py) | Easy | O(N) | O(N) | Array | There is a better solution | |
| 1471 | [The k Strongest Values in an Array](src/1471.the-k-strongest-values-in-an-array.py) | Medium | O(NlogN) | O(N) | Array, Sort | There is a better solution | |
| 1472 | [Design Browser History](src/1472.design-browser-history.py) | Medium | O(1) | O(1) | Design | | |
| 1474 | [Delete N Nodes After M Nodes of a Linked List](src/1474.py) | Easy | O(N) | O(1) | Linked List, Premium | | 🔒 |
| 1475 | [Final Prices With a Special Discount in a Shop](src/1475.final-prices-with-a-special-discount-in-a-shop.py) | Easy | O(N) | O(1) | Monotonic Stack | | |
| 1476 | [Subrectangle Queries](src/1476.subrectangle-queries.py) | Easy | Varying | Varying | Design | | |
| 1480 | [Running Sum of 1d Array](src/1480.running-sum-of-1-d-array.py) | Easy | O(N) | O(1) | | | |
| 1481 | [Least Number of Unique Integers after K Removals](src/1481.least-number-of-unique-integers-after-k-removals.py) | Medium | O(NlogN) | O(N) | Array, Sort | | |
| 1482 | [Minimum Number of Days to Make m Bouquets](src/1482.minimum-number-of-days-to-make-m-bouquets.py) | Medium | O(NlogN) | O(N) | Array, Binary Search | | |
| 1486 | [XOR Operation in an Array](src/1486.xor-operation-in-an-array.py) | Easy | O(1) | O(1) | Bit Manipulation | | |
| 1491 | [Average Salary Excluding the Minimum and Maximum Salary](src/1491.average-salary-excluding-the-minimum-and-maximum-salary.py) | Easy | O(N) | O(1) | | | |
| 1492 | [The kth Factor of n](src/1492.the-kth-factor-of-n.py) | Medium | O(logN) | O(logN) | Math, Tricky | | |
| 1493 | [Longest Subarray of 1's After Deleting One Element](src/1493.longest-subarray-of-1-s-after-deleting-one-element.py) | Medium | O(N) | O(1) | Array | | |
| 1496 | [Path Crossing](src/1496.path-crossing.py) | Easy | O(N) | O(N) | String | | |
| 1502 | [Can Make Arithmetic Progression From Sequence](src/1502.can-make-arithmetic-progression-from-sequence.py) | Easy | O(NlogN) | O(1) | Array | | |
| 1507 | [Reformat Date](src/1507.reformat-date.py) | Easy | O(1) | O(1) | String | | |
| 1508 | [Range Sum of Sorted Subarray Sums](src/1508.range-sum-of-sorted-subarray-sums.py) | Medium | O(N^2logN) | O(N^2) | | | |
| 1509 | [Minimum Difference Between Largest and Smallest Value in Three Moves](src/1509.minimum-difference-between-largest-and-smallest-value-in-three-moves.py) | Medium | O(NlogN) | O(1) | | | |
| 1510 | [Stone Game IV](src/1510.stone-game-iv.py) | Hard | O(N*N^0.5) | O(N) | Dynamic Programming | | |
| 1512 | [Number of Good Pairs](src/1512.number-of-good-pairs.py) | Easy | O(N) | O(N) | | | |
| 1513 | [Number of Substrings With Only 1s](src/1513.number-of-substrings-with-only-1-s.py) | Medium | O(N) | O(N) | String, Math | | |
| 1518 | [Water Bottles](src/1518.water-bottles.py) | Easy | O(1) | O(1) | Greedy, Simulation | | |
| 1523 | [Count Odd Numbers in an Interval Range](src/1523.count-odd-numbers-in-an-interval-range.py) | Easy | O(1) | O(1) | Math | | |
| 1524 | [Number of Sub-arrays With Odd Sum](src/1524.number-of-sub-arrays-with-odd-sum.py) | Medium | O(N) | O(1) | Array, Math, Dynamic Programming | | |
| 1525 | [Number of Good Ways to Split a String](src/1525.number-of-good-ways-to-split-a-string.py) | Medium | O(N) | O(N) | String | | |
| 1528 | [Shuffle String](src/1528.shuffle-string.py) | Easy | O(N) | O(N) | String | | |
| 1529 | [Bulb Switcher IV](src/1529.bulb-switcher-iv.py) | Medium | O(N) | O(1) | String | | |
| 1530 | [Number of Good Leaf Nodes Pairs](src/1530.number-of-good-leaf-nodes-pairs.py) | Medium | O(N^2logN) | O(N) | Tree, DFS | | |
| 1533 | [Find the Index of the Large Integer](src/1533.py) | Medium | O(logN) | O(1) | Premium, Binary Search | | 🔒 |
| 1535 | [Find the Winner of an Array Game](src/1535.find-the-winner-of-an-array-game.py) | Medium | O(N) | O(1) | Array | | |
| 1539 | [Kth Missing Positive Number](src/1539.kth-missing-positive-number.py) | Easy | O(logN) | O(1) | Binary Search | | |
| 1544 | [Make The String Great](src/1544.make-the-string-great.py) | Easy | O(N) | O(N) | String, Stack | | |
| 1545 | [Find Kth Bit in Nth Binary String](src/1545.find-kth-bit-in-nth-binary-string.py) | Medium | O(N^2) | O(N^2) | String | Not Optimal | |
| 1550 | [Three Consecutive Odds](src/1550.three-consecutive-odds.py) | Easy | O(N) | O(1) | Array | | |
| 1551 | [Minimum Operations to Make Array Equal](src/1551.minimum-operations-to-make-array-equal.py) | Medium | O(1) | O(1) | Math | | |
| 1552 | [Magnetic Force Between Two Balls](src/1552.magnetic-force-between-two-balls.py) | Medium | O(NlogN) | O(1) | Binary Search | Template for Binary Search | |
| 1556 | [Thousand Separator](src/1556.thousand-separator.py) | Easy | O(N) | O(N) | String | | |
| 1557 | [Minimum Number of Vertices to Reach All Nodes](src/1557.minimum-number-of-vertices-to-reach-all-nodes.py) | Medium | O(N) | O(N) | Graph | | |
| 1558 | [Minimum Numbers of Function Calls to Make Target Array](src/1558.minimum-numbers-of-function-calls-to-make-target-array.py) | Medium | O(NlogK) | O(N) | Greedy, Simulation | | |
| 1560 | [Most Visited Sector in a Circular Track](src/1560.most-visited-sector-in-a-circular-track.py) | Easy | O(N) | O(1) | Array | | |
| 1561 | [Maximum Number of Coins You Can Get](src/1561.maximum-number-of-coins-you-can-get.py) | Medium | O(N) | O(1) | Sort | | |
| 1564 | [Put Boxes Into the Warehouse I](src/1564.py) | Medium | O(NlogN) | O(N) | Greedy | | 🔒 |
| 1566 | [Detect Pattern of Length M Repeated K or More Times](src/1566.detect-pattern-of-length-m-repeated-k-or-more-times.py) | Easy | O(N) | O(1) | Array | | |
| 1572 | [Matrix Diagonal Sum](src/1572.matrix-diagonal-sum.py) | Easy | O(N) | O(1) | Array | | |
| 1573 | [Number of Ways to Split a String](src/1573.number-of-ways-to-split-a-string.py) | Medium | O(N) | O(N) | String | | |
| 1576 | [Replace All ?'s to Avoid Consecutive Repeating Characters](src/1576.replace-all-s-to-avoid-consecutive-repeating-characters.py) | Easy | O(N) | O(N) | String | | |
| 1578 | [Minimum Deletion Cost to Avoid Repeating Letters](src/1578.minimum-deletion-cost-to-avoid-repeating-letters.py) | Medium | O(N) | O(1) | Greedy | | |
| 1580 | [Put Boxes Into the Warehouse II](src/1580.py) | Medium | O(NlogN) | O(N) | Greedy | | 🔒 |
| 1582 | [Special Positions in a Binary Matrix](src/1582.special-positions-in-a-binary-matrix.py) | Easy | O(N) | O(N) | Array | | |
| 1583 | [Count Unhappy Friends](src/1583.count-unhappy-friends.py) | Medium | O(N^2) | O(N^2) | Array | | |
| 1588 | [Sum of All Odd Length Subarrays](src/1588.sum-of-all-odd-length-subarrays.py) | Easy | O(N) | O(1) | Array | | |
| 1592 | [Rearrange Spaces Between Words](src/1592.rearrange-spaces-between-words.py) | Easy | O(N) | O(N) | String | | |
| 1598 | [Crawler Log Folder](src/1598.crawler-log-folder.py) | Easy | O(N) | O(1) | Stack | | |
| 1600 | [Throne Inheritance](src/1600.throne-inheritance.py) | Medium | O(N) | O(N) | Tree, Design | | |
| 1602 | [Find Nearest Right Node in Binary Tree](src/1602.py) | Medium | O(N) | O(N) | Premium, Tree, BFS | | 🔒 |
| 1604 | [Alert Using Same Key-Card Three or More Times in a One Hour Period](src/1604.alert-using-same-key-card-three-or-more-times-in-a-one-hour-period.py) | Medium | O(NlogN) | O(N) | String, Ordered Map | | |
| 1605 | [Find Valid Matrix Given Row and Column Sums](src/1605.find-valid-matrix-given-row-and-column-sums.py) | Medium | O(NM) | O(NM) | Greedy | | |
| 1608 | [Special Array With X Elements Greater Than or Equal X](src/1608.special-array-with-x-elements-greater-than-or-equal-x.py) | Easy | O(NlogN) | O(N) | Binary Search, Array | | |
| 1609 | [Even Odd Tree](src/1609.even-odd-tree.py) | Easy | O(N) | O(N) | Tree | | |
| 1614 | [Maximum Nesting Depth of the Parentheses](src/1614.maximum-nesting-depth-of-the-parentheses.py) | Easy | O(N) | O(1) | String | | |
| 1615 | [Maximal Network Rank](src/1615.maximal-network-rank.py) | Medium | O(N) | O(1) | Graph | | |
| 1618 | [Maximum Font to Fit a Sentence in a Screen](src/1618.py) | Medium | O(logN) | O(1) | Premium, String, Binary Search | | 🔒 |
| 1624 | [Largest Substring Between Two Equal Characters](src/1624.largest-substring-between-two-equal-characters.py) | Easy | O(N) | O(1) | String | | |
| 1625 | [Lexicographically Smallest String After Applying Operations](src/1625.lexicographically-smallest-string-after-applying-operations.py) | Medium | O(N*N) | O(N) | BFS, DFS | | |
| 1629 | [Slowest Key](src/1629.slowest-key.py) | Easy | O(N) | O(1) | String | | |
| 1631 | [Path With Minimum Effort](src/1631.path-with-minimum-effort.py) | Medium | O(N\*M\*logH) | O(M\*N) | Binary Search, DFS, BFS, Union Find, Graph | | |
| 1634 | [Add Two Polynomials Represented as Linked Lists](src/1634.py) | Medium | O(N) | O(1) | Premium, Linked List | | 🔒 |
| 1639 | [Number of Ways to Form a Target String Given a Dictionary](src/1639.number-of-ways-to-form-a-target-string-given-a-dictionary.py) | Hard | O(N\*M) | O(N\*M) | Dynamic Programming | | |
| 1640 | [Check Array Formation Through Concatenation](src/1640.check-array-formation-through-concatenation.py) | Medium | O(N) | O(N) | Array | | |
| 1641 | [Count Sorted Vowel Strings](src/1641.count-sorted-vowel-strings.py) | Medium | O(N) | O(1) | Dynamic Programming, Math, Backtracking | | |
| 1642 | [Furthest Building You Can Reach](src/1642.furthest-building-you-can-reach.py) | Medium | O(NlogN) | O(N) | Binary Search, Heap | | |
| 1644 | [Lowest Common Ancestor of a Binary Tree II](src/1644.py) | Medium | O(N) | O(H) | Premium, Tree | | 🔒 |
| 1646 | [Get Maximum in Generated Array](src/1646.get-maximum-in-generated-array.py) | Easy | O(N) | O(N) | Array | | |
| 1647 | [Minimum Deletions to Make Character Frequencies Unique](src/1647.minimum-deletions-to-make-character-frequencies-unique.py) | Medium | O(1) | O(1) | Greedy, Sort | | |
| 1650 | [Lowest Common Ancestor of a Binary Tree III](src/1650.py) | Medium | O(H) | O(1) | Premium, Tree | | 🔒 |
| 1652 | [Defuse the Bomb](src/1652.defuse-the-bomb.py) | Medium | O(N) | O(N) | Array | | |
| 1653 | [Minimum Deletions to Make String Balanced](src/1653.minimum-deletions-to-make-string-balanced.py) | Medium | O(N) | O(N) | Greedy, String | | |
| 1656 | [Design an Ordered Stream](src/1656.design-an-ordered-stream.py) | Easy | O(N) | O(N) | Array, Design | | |
| 1657 | [Determine if Two Strings Are Close](src/1657.determine-if-two-strings-are-close.py) | Medium | O(N) | O(1) | Greedy | | |
| 1658 | [Minimum Operations to Reduce X to Zero](src/1658.minimum-operations-to-reduce-x-to-zero.py) | Medium | O(N) | O(N) | Greedy, Sliding Window | | |
| 1663 | [Smallest String With A Given Numeric Value](src/1663.smallest-string-with-a-given-numeric-value.py) | Medium | O(N) | O(1) | Greedy | | |
| 1664 | [Ways to Make a Fair Array](src/1664.ways-to-make-a-fair-array.py) | Medium | O(N) | O(1) | Dynamic Programming, Greedy | | |
| 1673 | [Find the Most Competitive Subsequence](src/1673.find-the-most-competitive-subsequence.py) | Medium | O(N) | O(K) | Stack, Heap, Greedy, Queue | | |
| 1679 | [Max Number of K-Sum Pairs](src/1679.max-number-of-k-sum-pairs.py) | Medium | O(N) | O(N) | Hash Table | | |
| 1684 | [Count the Number of Consistent Strings](src/1684.count-the-number-of-consistent-strings.py) | Easy | O(N) | O(1) | String | | |
| 1685 | [Sum of Absolute Differences in a Sorted Array](src/1685.sum-of-absolute-differences-in-a-sorted-array.py) | Medium | O(N) | O(N) | Math, Greedy | | |
| 1690 | [Stone Game VII](src/1690.stone-game-vii.py) | Medium | O(N^2) | O(N^2) | Dynamic Programming | | |
| 1695 | [Maximum Erasure Value](src/1695.maximum-erasure-value.py) | Medium | O(N) | O(1) | Two Pointers | | |
| 1696 | [Jump Game VI](src/1696.jump-game-vi.py) | Medium | O(N) | O(N) | Dequeue | Dequeue, Monotonic Dequeue | |
| 1700 | [Number of Students Unable to Eat Lunch](src/1700.number-of-students-unable-to-eat-lunch.py) | Medium | O(N) | O(1) | Array | | |
| 1705 | [Maximum Number of Eaten Apples](src/1705.maximum-number-of-eaten-apples.py) | Medium | O(NlogN) | O(N) | Heap, Greedy | | |
| 1706 | [Where Will the Ball Fall](src/1706.where-will-the-ball-fall.py) | Medium | O(N*M) | O(M) | Dynamic Programming | | |
| 1710 | [Maximum Units on a Truck](src/1710.maximum-units-on-a-truck.py) | Medium | O(NlogN) | O(N) | Greedy, Sort | | |
| 1716 | [Calculate Money in Leetcode Bank](src/1716.calculate-money-in-leetcode-bank.py) | Easy | O(N) | O(1) | Math, Greedy | | |
| 1721 | [Swapping Nodes in a Linked List](src/1721.swapping-nodes-in-a-linked-list.py) | Medium | O(N) | O(1) | Linked List | | |
| 1725 | [Number Of Rectangles That Can Form The Largest Square](src/1725.number-of-rectangles-that-can-form-the-largest-square.py) | Easy | O(N) | O(1) | Greedy | | |
| 1726 | [Tuple with Same Product](src/1726.tuple-with-same-product.py) | Medium | O(N^2) | O(N) | Array, Hash Table | | |
| 1732 | [Find the Highest Altitude](src/1732.find-the-highest-altitude.py) | Easy | O(N) | O(1) | Array | | |
| 1736 | [Latest Time by Replacing Hidden Digits](src/1736.latest-time-by-replacing-hidden-digits.py) | Easy | O(1) | O(1) | String, Greedy | | |
| 1748 | [Sum of Unique Elements](src/1748.sum-of-unique-elements.py) | Easy | O(N) | O(N) | Array, Hash Table | | |
| 1749 | [Maximum Absolute Sum of Any Subarray](src/1749.maximum-absolute-sum-of-any-subarray.py) | Medium | O(N) | O(1) | Greedy | | |
| 1750 | [Minimum Length of String After Deleting Similar Ends](src/1750.minimum-length-of-string-after-deleting-similar-ends.py) | Medium | O(N) | O(1) | Two Pointers | | |
| 1752 | [Check if Array Is Sorted and Rotated](src/1752.check-if-array-is-sorted-and-rotated.py) | Easy | O(N) | O(1) | Array | | |
| 1753 | [Maximum Score From Removing Stones](src/1753.maximum-score-from-removing-stones.py) | Medium | O(1) | O(1) | Math, Heap | | |
| 1758 | [Minimum Changes To Make Alternating Binary String](src/1758.minimum-changes-to-make-alternating-binary-string.py) | Easy | O(N) | O(1) | Array, Greedy | | |
| 1759 | [Count Number of Homogenous Substrings](src/1759.count-number-of-homogenous-substrings.py) | Medium | O(N) | O(1) | String, Greedy | | |
| 1763 | [Longest Nice Substring](src/1763.longest-nice-substring.py) | Easy | O(NlogN) | O(N) | String | | |
| 1764 | [Form Array by Concatenating Subarrays of Another Array](src/1764.form-array-by-concatenating-subarrays-of-another-array.py) | Medium | O(N+M) | O(M) | Array, Greedy | New Algorithm (KMP) | |
| 1765 | [Map of Highest Peak](src/1765.map-of-highest-peak.py) | Medium | O(N\*M) | O(N\*M) | BFS, Graph | | |
| 1768 | [Merge Strings Alternately](src/1768.merge-strings-alternately.py) | Easy | O(N) | O(N) | String | | |
| 1769 | [Minimum Number of Operations to Move All Balls to Each Box](src/1769.minimum-number-of-operations-to-move-all-balls-to-each-box.py) | Medium | O(N) | O(N) | Array, Greedy | | |
| 1773 | [Count Items Matching a Rule](src/1773.count-items-matching-a-rule.py) | Easy | O(N) | O(1) | Array, String | | |
| 1774 | [Closest Dessert Cost](src/1774.closest-dessert-cost.py) | Medium | O(N\*M\*V) | O(M\*V) | Greedy | | |
| 1779 | [Find Nearest Point That Has the Same X or Y Coordinate](src/1779.find-nearest-point-that-has-the-same-x-or-y-coordinate.py) | Easy | O(N) | O(1) | Array | | |
| 1780 | [Check if Number is a Sum of Powers of Three](src/1780.check-if-number-is-a-sum-of-powers-of-three.py) | Medium | O(logN) | O(1) | Math, Backtracking, Recursion | | |
| 1781 | [Sum of Beauty of All Substrings](src/1781.sum-of-beauty-of-all-substrings.py) | Medium | O(N^2) | O(1) | Hash Table, String | | |
| 1784 | [Check if Binary String Has at Most One Segment of Ones](src/1784.check-if-binary-string-has-at-most-one-segment-of-ones.py) | Easy | O(N) | O(1) | Greedy | | |
| 1791 | [Find Center of Star Graph](src/1791.find-center-of-star-graph.py) | Medium | O(1) | O(1) | Graph | | |
| 1792 | [Maximum Average Pass Ratio](src/1792.maximum-average-pass-ratio.py) | Medium | O(N+KlogN) | O(N) | Heap | | |
| 1797 | [Design Authentication Manager](src/1797.design-authentication-manager.py) | Medium | O(Design) | O(N) | Hash Table, Design | | |
| 1816 | [Truncate Sentence](src/1816.truncate-sentence.py) | Easy | O(N) | O(1) | String | | |
| 1818 | [Minimum Absolute Sum Difference](src/1818.minimum-absolute-sum-difference.py) | Medium | O(NlogN) | O(sort) | Binary Search, Greedy | | |
| 1827 | [Minimum Operations to Make the Array Increasing](src/1827.minimum-operations-to-make-the-array-increasing.py) | Easy | O(N) | O(1) | Array, Greedy | | |
| 1828 | [Queries on Number of Points Inside a Circle](src/1828.queries-on-number-of-points-inside-a-circle.py) | Medium | O(N*M) | O(M) | Math | | |
| 1832 | [Check if the Sentence Is Pangram](src/1832.check-if-the-sentence-is-pangram.py) | Easy | O(N) | O(1) | String | | |
| 1833 | [Maximum Ice Cream Bars](src/1833.maximum-ice-cream-bars.py) | Medium | O(NlogN) | O(sort) | Array, Sort | | |
| 1837 | [Sum of Digits in Base K](src/1837.sum-of-digits-in-base-k.py) | Medium | O(logN) | O(1) | Math, Bit Manipulation | | |
| 1839 | [Longest Substring Of All Vowels in Order](src/1839.longest-substring-of-all-vowels-in-order.py) | Medium | O(N) | O(1) | Two Pointers, String | | |
| 1844 | [Replace All Digits with Characters](src/1844.replace-all-digits-with-characters.py) | Easy | O(N) | O(N) | String | | |
| 1845 | [Seat Reservation Manager](src/1845.seat-reservation-manager.py) | Medium | O(logN) | O(N) | Heap, Design | | |
| 1848 | [Minimum Distance to the Target Element](src/1848.minimum-distance-to-the-target-element.py) | Easy | O(N) | O(1) | Array | | |
| 1854 | [Maximum Population Year](src/1854.maximum-population-year.py) | Easy | O(NlogN) | O(N) | Array, Counting | | |
| 1860 | [Incremental Memory Leak](src/1860.incremental-memory-leak.py) | Medium | O(logN) | O(1) | Math | | |
| 1861 | [Rotating the Box](src/1861.rotating-the-box.py) | Medium | O(R\*C) | O(1) | Array, Two Pointers | | |
| 1899 | [Merge Triplets to Form Target Triplet](src/1899.merge-triplets-to-form-target-triplet.py) | Medium | O(N) | O(1) | Greedy, Array | | |

# Useful Posts:

- [Important and Useful links from all over the LeetCode](https://leetcode.com/discuss/general-discussion/665604/Important-and-Useful-links-from-all-over-the-LeetCode)
- [Graph](https://leetcode.com/discuss/general-discussion/655708/Graph-For-Beginners-Problems-or-Pattern-or-Sample-Solutions)
- [Sliding Windows](https://leetcode.com/discuss/general-discussion/657507/Sliding-Window-for-Beginners-Problems-or-Template-or-Sample-Solutions)
- [Trie](https://leetcode.com/discuss/general-discussion/680706/Article-on-Trie.-General-Template-and-List-of-problems)
- [Graph](https://leetcode.com/discuss/general-discussion/969327/graph-algorithms-one-place-dijkstra-bellman-ford-floyd-warshall-prims-kruskals-dsu)
- [Template for Hard String Problems](https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems)
- [Powerful studying program for Beginners and Intermediate levels. All common mistakes analyzed.](https://leetcode.com/discuss/general-discussion/1129503/powerful-studying-program-for-beginners-and-intermediate-levels-all-common-mistakes-analyzed)
- [Bit Hacks](https://leetcode.com/discuss/study-guide/1151183/TIPS-or-HACKS-WHICH-YOU-CAN'T-IGNORE-AS-A-CODER)
- [Tips and Tricks](https://leetcode.com/discuss/study-guide/1177039/%22Practice-More-Learn-More%22-greater-Study-Guide-and-Interview-Preparation-Using-LEETCODE)

## Syntax:

- [C++](https://leetcode.com/discuss/study-guide/1154632/C%2B%2B-STL-powerful-guide-or-Compiled-list-of-popular-STL-operations)
- [Java](https://leetcode.com/discuss/study-guide/1170715/Java-or-Data-Structure-Mostly-used-Syntax)

## Dynamic Programming

- https://leetcode.com/discuss/general-discussion/662866/dp-for-beginners-problems-patterns-sample-solutions
- https://leetcode.com/discuss/interview-question/491522/dynamic-programming-questions-thread
- https://leetcode.com/discuss/general-discussion/458695/Dynamic-Programming-Patterns
- https://leetcode.com/discuss/general-discussion/868902/dynamic-programming
- https://leetcode.com/discuss/general-discussion/1081421/powerful-dynamic-programming-explanation

## System Design

- [✅ Helpful list of LeetCode Posts on System Design at Facebook, Google, Amazon, Uber, Microsoft](https://leetcode.com/discuss/interview-question/1140451/helpful-list-of-leetcode-posts-on-system-design-at-facebook-google-amazon-uber-microsoft)
- https://leetcode.com/discuss/interview-question/1177601/Flipkart-or-Machine-Coding-or-Design-Online-Coding-Platform-CODING-BLOX-Leetcode-LLD

## LP

- [Amazon LPs Compiled](https://leetcode.com/discuss/interview-experience/1149636/amazon-lps-compiled)

## Others

- https://leetcode.com/discuss/general-discussion/705117/requesting-guidance-from-those-who-solved-1000-leets-so-far

## List

- [Amazon Questions](https://leetcode.com/list/5ecpr1th/)
