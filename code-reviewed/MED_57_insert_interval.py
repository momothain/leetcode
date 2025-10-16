from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """blind rewrite 10/16 to reason out base, edge cases, practice testing"""
        #non lap, start,end. asc order. newint
        #maintain order. merge new overlaps

        # algo: check each interval,
        # - if newinterval starts before end of curr interval
        #   - a. insert before
        #   - b. merge and propagate merge forward
        # mode flag: inserting or merging
        inserted = False
        out = []
        
        for curr_int in intervals:
            if newInterval[0] <= curr_int[1]: #somewhere b4
                if curr_int[0]<= newInterval[1]: #overlap
                    #merge regardless of insert; skip insert curr_int cuz new handles merge
                    newInterval[0] = min(newInterval[0], curr_int[0])
                    newInterval[1] = max(newInterval[1], curr_int[1])
                    if not inserted:
                        out.append(newInterval)
                        inserted = True
                else: #before
                    if not inserted:
                        out.append(newInterval)
                        inserted = True
                    out.append(curr_int)
            else:
                out.append(curr_int)
                
        # Base case: starts after end of all curr intervals
        if not inserted:
            out.append(newInterval)
        
        return out



    def test_insert(self):
        # empty
        intervals = []
        newInterval = [7,8]
        out = [[7,8]]
        assert(self.insert(intervals, newInterval) == out)
        intervals = []
        newInterval = [0,0]
        out = [[0,0]]
        # print(self.insert(intervals, newInterval))
        assert(self.insert(intervals, newInterval) == out)


        #base self.insert end
        intervals = [[0,2], [3,5]]
        newInterval = [7,8]
        out = [[0,2], [3,5], [7,8]]
        print(self.insert(intervals, newInterval))
        assert(self.insert(intervals, newInterval) == out)

        #self.insert before, 0 start, adj not overlap
        intervals = [[4,5]]
        newInterval = [0,3]
        out = [[0,3], [4,5]]
        assert(self.insert(intervals, newInterval) == out)
        
        #overlap 1 merge
        if True:
            #merge before, barely adjacent
            intervals = [[4,5]]
            newInterval = [0,4]
            out = [[0,5]]
            assert(self.insert(intervals, newInterval) == out)
            
            #merge =
            intervals = [[1,5]]
            newInterval = [1,5]
            out = [[1,5]]
            assert(self.insert(intervals, newInterval) == out)
            #merge after
            ...
            #merge contains

        #overlap 2+ merge
        intervals = [[4,5], [6,7]]
        newInterval = [0,7]
        out = [[0,7]]
        assert(self.insert(intervals, newInterval) == out)









    def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #non-verlap
        #sorted asc 
        #insert newInt, maintain asc order, merge overlapping intervals if necessary!!
        #not inplace
        if not intervals:
            return [newInterval]

        # idea: compare new start against all ends
        new_ls = []
        inserted = False

        #base case? redundant?
        # if newInterval[0] < intervals[0][0]:
            # insert before w/ merge check on end

        # better with binary search?
        for i, interval in enumerate(intervals):
            if newInterval[0] <= interval[1]: #then merge here and check after/end
                if interval[0] <= newInterval[1]: #start is before end, and end is after start means they actually overlap
                    newInterval[0] = min(interval[0], newInterval[0])
                    newInterval[1] = max(interval[1], newInterval[1])
                    
                    if not inserted:
                        new_ls.append(newInterval) #and skip the curr interval
                        inserted = True
                    # continue to merge w/ rest but not append
                else: # it is completely before interval and not overlapping
                    if not inserted:
                        new_ls.append(newInterval)
                    new_ls.extend(intervals[i:]) #rest
                    return new_ls
            else:
                new_ls.append(interval)
        if not inserted:
            new_ls.append(newInterval)
        return new_ls


# if __name__ == "__main__":
#     s = Solution()
#     s.test_insert()
    
# chatgpt idea
if __name__ == "__main__":
    s = Solution()
    tests = [
        ([], [7,8], [[7,8]]),
        ([[0,2],[3,5]], [7,8], [[0,2],[3,5],[7,8]]),
        ([[4,5]], [0,3], [[0,3],[4,5]]),
        ([[4,5]], [0,4], [[0,5]]),
    ]
    for intervals, newInterval, expected in tests:
        result = s.insert(intervals, newInterval)
        assert result == expected, f"Fail: {intervals=} {newInterval=} got {result} expected {expected}"
    print("✅ All passed")