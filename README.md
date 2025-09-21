# leetcode
any coding practice problems actually, but default (direct difficulty subdirectories) is leetcode.

code-reviewed means I spent time reviewing and improving the code after initially trying to solve the problem w/ time constraints, e.g. [Flood Fill](https://github.com/momothain/leetcode/blob/bf5a4ac2258e09c504a582ee8a644b86d66682d8/code-reviewed/EASY_733_flood_fill.py)

## General Notes

### [Flood Fill, 9/21/25](https://github.com/momothain/leetcode/blob/bf5a4ac2258e09c504a582ee8a644b86d66682d8/code-reviewed/EASY_733_flood_fill.py)
- collections.deque for BFS for const popleft, append.
- for e.g. Set[], Tuple IS hashable. List is not.
- tendency to overiterate recursion logic, e.g. do two layers of recursion manually instead of trust the loops logic.
- structural validity (well-formedness, safety conditions) (e.g. bounds, type) FIRST, then semantic/domain condition checks after.
