"""https://leetcode.com/problems/maximum-subarray/description/
Accepted
210 / 210 testcases passed
Morgann Thain
Morgann Thain
submitted at Sep 26, 2025 16:04

Editorial

Solution
Runtime
79
ms
Beats
48.91%
Analyze Complexity
Memory
31.62
MB
Beats
95.94%

"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # subarray means sliding window. empty not allowed
        # base case [n] -> sum = n.
        # assume we have the greatest subarray possible so far.

        # if it's (-) (is that possible), we should skip the whole thing

        # should we shrink from the left, or expand to the right?
        # We shrink if we think there's a leading subarray within us that's negative
        # maybe we never shrink, because we know we've skipped all negative subarrays already? Especially if it's leading, we can only have reached it through having directly looked at it, and grown instead of skipping, which we can assume we never do
        # e.g. at ex3: [5,4,-1], we obviously add 5,4 cuz they're positive, then we must add -1 because we want to keep the positive sum we have so far, so then we just keep adding and get [5,4,-1,7,8]

        left = 0
        right = 1 #not inclusive
        curr_sum =  nums[0]
        max_sum = nums[0]
        # max_arr = (left, right)
        print(nums)
        while right < len(nums): # stop one early because the loop assumes the current array is checked and it needs to increase the right size by one
            ### pr
            # print(left,",",right)
            # print("curr_sum: ", curr_sum)
            # print("max_sum: ", max_sum)
            ### iterate
            # negative skip case
            if curr_sum <= 0:
                left = right
                right += 1 # to me it is visually more intuitive to expand the end of the window past the next index we're going to include, the update the sum based on the new index which is now right-1
                # if (right - 1) < len(nums): #simplified after reducing the loop
                curr_sum = nums[right - 1] #left is okay here
            else:
            # normal grow right
                right += 1
                # if (right - 1) < len(nums): #^^
                curr_sum += nums[right - 1]

            ### check max
            if curr_sum > max_sum: # would be max_sum = max(curr_sum, max_sum) if not for debugging purposes
                max_sum = curr_sum
                # max_arr = (left, right)
            
        return max_sum

    def ThirtyminishAndAccepted(self, nums: List[int]) -> int:
        """over-complicated loop / end condition checks. didn't recognize"""
        left = 0
        right = 1 #not inclusive
        curr_sum =  nums[0]
        max_sum = nums[0]
        # max_arr = (left, right)
        print(nums)
        while right <= len(nums):
            ### pr
            # print(left,",",right)
            # print("curr_sum: ", curr_sum)
            # print("max_sum: ", max_sum)
            ### iterate
            # negative skip case
            if curr_sum <= 0:
                left = right
                right += 1
                if (right - 1) < len(nums):
                    curr_sum = nums[right - 1]
            else:
            # normal grow right
                right += 1
                if (right - 1) < len(nums):
                    curr_sum += nums[right - 1]

            ### check max
            if curr_sum > max_sum:
                max_sum = curr_sum
                # max_arr = (left, right)
            
        return max_sum

    def FirstAndWrongmaxSubArray(self, nums: List[int]) -> int:
        """bad setting curr_sum to default -1 at the end, but the true max_sum could be negative and lower causing the wrong answer.
        setting curr_sum to 0 also won't work if we don't override it"""
        right = 1 #not inclusive
        curr_sum =  nums[0]
        max_sum = nums[0]
        max_arr = (left, right)
        print(nums)
        while right <= len(nums):
            ### pr
            print(left,",",right)
            print("curr_sum: ", curr_sum)
            print("max_sum: ", max_sum)
            ### iterate
            # negative skip case
            if curr_sum <= 0:
                left = right
                curr_sum = 0
            # grow right (no matter what)
            right += 1
            
            if (right - 1) < len(nums):
                curr_sum += nums[right - 1]
            else: #not necessary but for clarity
                curr_sum = -1

            ### check max
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_arr = (left, right)
            
        return max_sum






# aug 11 accepted first try
    def AmaxSubArray(self, nums: List[int]) -> int:
        # def main(nums: List[int]) -> int:
        if not nums:
            return 0

        left = 0; right = 1
        curr_sum = nums[0]
        max_sum = nums[0]
        #[|0|,1,2,...]
        # too early end cond? last step? [-1,-2,-3,7]?
        while right < len(nums):
            # curr sum is negative -> incr left
            if curr_sum <= 0:
                left += 1
                
                # redundant? don't let left pass right
                if right <= left:
                    right = left + 1
                    curr_sum = nums[left]
                else:
                    curr_sum -= nums[left-1]

            #  incr right .. max lennums
            # elif(right)
            else:
                right += 1
                curr_sum += nums[right - 1]
                

            max_sum = max(max_sum, curr_sum)
        
        return max_sum



    

