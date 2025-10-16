# leetcode
any coding practice problems actually, but default (direct difficulty subdirectories) is leetcode.

code-reviewed means I spent time reviewing and improving the code after initially trying to solve the problem w/ time constraints, e.g. [Flood Fill](https://github.com/momothain/leetcode/blob/bf5a4ac2258e09c504a582ee8a644b86d66682d8/code-reviewed/EASY_733_flood_fill.py)

## General Notes
### [57. Insert Interval]()
- edge cases not covered at all w/o test cases....
- need to check loop/special/insert conditions all the time
- need to check very start/end things
- great one to practice testing on


### [232. Implement Queue using Stacks, 10/15/25](https://github.com/momothain/leetcode/blob/main/easy/232-queue-via-stacks.py)
- "Class Attributes" - Initializing fields in the Class fields causes them to not reset between tests/instantiations
- put them in __init__() instead

### [Lowest Common Ancestor of a Binary Search Tree, 9/25,29/25](https://github.com/momothain/leetcode/blob/main/code-reviewed/MED_235_lca_bst.py)
- Be really careful that most .operations() are in place modifiers and not functional. I did `return [root.val].append(left)` for recursion and that always returns None.

### [Max Subarray, 9/25,29/25](https://github.com/momothain/leetcode/blob/main/code-reviewed/MED_53_maximum_subarray.py)
- Simplify end conditions by understanding what the loop is assuming in terms of induction. Checking end of list twice is a Red Flag. 
- Ensure defaults are truly minimum/maximum esp when 'setting after the loop for style (bc my loop end conditions were overcomplicated)'

### [Flood Fill, 9/21/25](https://github.com/momothain/leetcode/blob/bf5a4ac2258e09c504a582ee8a644b86d66682d8/code-reviewed/EASY_733_flood_fill.py)
- collections.deque for BFS for const popleft, append.
- for e.g. Set[], Tuple IS hashable. List is not.
- tendency to overiterate recursion logic, e.g. do two layers of recursion manually instead of trust the loops logic.
- structural validity (well-formedness, safety conditions) (e.g. bounds, type) FIRST, then semantic/domain condition checks after.
