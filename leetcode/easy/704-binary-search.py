"""Accepted
47 / 47 testcases passed
Morgann Thain
Morgann Thain
submitted at Sep 17, 2025 18:39

Editorial

Solution
Runtime
0
ms
Beats
100.00%
Analyze Complexity
Memory
18.76
MB
Beats
44.87%"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # does middle require even/odd handling?
        start = 0
        end = len(nums) - 1

        while start < end:
            curr_len = end - start + 1
            mid_i = start + (curr_len // 2) #rounded down
            if target == nums[mid_i]:
                return mid_i
            elif target < nums[mid_i]:
                end = mid_i - 1
            else:
                start = mid_i + 1
            
            # round down len 2 overflow
            if start >= len(nums):
                return -1
        
        #start == end

        if nums[start] == target:
            return start
        else:
            return -1