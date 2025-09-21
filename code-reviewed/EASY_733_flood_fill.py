"""https://leetcode.com/problems/flood-fill/
30min code stats below. 1hr+ on review code and comments below used gpt link: https://chatgpt.com/share/68d04e4f-f7b0-8013-97d6-627bd76b77f7 .

Accepted
278 / 278 testcases passed
Morgann Thain
Morgann Thain
submitted at Sep 21, 2025 13:49

Editorial

Solution
Runtime
1
ms
Beats
25.04%
Analyze Complexity
Memory
18.06
MB
Beats
50.14%

"""
from collections import deque
class Solution:
    # AFTER REVIEW w/ solutions and gpt-5
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m,n = len(image), len(image[0]) #style add
        # You CAN just check the color, b/c if it's new color, then you don't recur from there ..... i thought you couldn't. no visited set needed IF we add the color == base_color termination case, since recoloring is the equivalent to visiting, but in that case it doesn't change 
        # breadth first search, starting at (sr,sc) 
        base_color = image[sr][sc]

        #weird edge case gpt found. can't change any colors because we only flood to colors...that are already the new color. code currently would iterate to them and change them redundantly.
        if color == base_color:
            return image
        
        # visited: Set[Tuple[int]] = {(sr,sc)} # Tuple IS hashable. list not
# type hint was wrong previously (didnt update to str)
        queue = deque([(sr,sc)]) 
        # change to clean/predictable traversal (set is unordered / set.pop() is random) for extensibility/debugging, though i could theoretically double queue a node before coloring it once to make it invalid, it will be skipped immediately since it's new color not old color
        # usually picked BFS as personal style > DFS, but they're equivalent here for correctness and in general for generic time/space complexity
        # BFS requires collections.deque for constant popleft (starto flist) and fully constant not amortized append
        # not recurring because that's heavier. explicit queue instead.
        # only pairs implicit type (len==2)
        while queue:
            r,c = queue.popleft()
            print(r,c)
            # print("p",p)
            # print("visited",visited)
            # print("queue",queue)

            # match og -> change & spread
            if image[r][c] != base_color:
                continue
            image[r][c] = color
            # up, right, down, left
            potential_adjacent = [
                (r - 1, c),
                (r, c + 1),
                (r + 1, c),
                (r, c - 1)]

            valid_adjacent = [(a,b) for a,b in potential_adjacent if (a >= 0 and a < m) and (b >= 0 and b < n) and (image[a][b] == base_color)] 
            # must put image (visited/relevance) check at end cuz bounds (structural validity) check must be first
            queue.extend(valid_adjacent)
        
        return image






    def floodFill30min(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def pair_to_str(p):
            a,b = p
            return f"{a},{b}"
        
        def str_to_pair(s: str) -> list[int]:
            a,b = s.split(",")
            return [int(a),int(b)]

        # print(f"pair_to_str test: {pair_to_str([1,2])}")
        # test2 = str_to_pair("1,2")
        # print(f"str_to_pair test: {test2}")
        # return



        # breadth first search, starting at (sr,sc) 
        base_color = image[sr][sc]
        visited: Set[List[int]] = {pair_to_str([sr,sc])} # string to represent the pair so it's hashable for Set
        queue: Set[List[int]] = {pair_to_str([sr,sc])} # only pairs implicit type
        while queue:
            p = queue.pop()
            print("p",p)
            print("visited",visited)
            print("queue",queue)
            r,c = str_to_pair(p)
            visited.add(p)
            # match og -> change & spread
            if image[r][c] == base_color:
                image[r][c] = color
                # up, right, down, left
                potential_adjacent = [
                    [r - 1, c],
                    [r, c + 1],
                    [r + 1, c],
                    [r, c - 1]]
                valid_adjacent = [pair_to_str([a,b]) for (a,b) in potential_adjacent if (not pair_to_str([a,b]) in visited) and (a >= 0 and a < len(image)) and (b >= 0 and b < len(image[0]))]
                queue.update(valid_adjacent)
            # if not match then just skip but it's still in the visited set
        
        return image


    def floodFill1(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # breadth first search, starting at (sr,sc) 
        # have to manually handle the direction of flood before recurring??
        # check if left,up,down,right exist now
        # left of curr changes and queues its up, left, down (not right because that's curr). etc. up down right. recur.
        # no its infinite

        # can't just check color changed. track a "visited" set.
        base_color = image[sr][sc]
        visited: Set[List[int]] = {[sr,sc]} # whether we changed it or not # TypeError: unhashable type: 'list' --->> make hashable custom Pair type or no set and handle duplicates/termination. or use a string to represent the pair.
        queue: Set[List[int]] = {[sr,sc]} # only pairs implicit type
        while queue:
            r,c = queue.pop()
            visited.add([r,c])
            # match og -> change & spread
            if image[r][c] == base_color:
                image[r][c] = color
                # up, right, down, left
                potential_adjacent = [
                    [r - 1, c]
                    [r, c + 1]
                    [r + 1, c]
                    [r, c - 1]]
                valid_adjacent = [[a,b] for (a,b) in potential_adjacent if (a >= 0 and a < len(image)) and (b >= 0 and b < len(image[0]))]
                queue.append(valid_adjacent)
            # if not match then just skip but it's still in the visited set
        
        return image



