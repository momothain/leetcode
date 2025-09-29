"""
Fucked myself and had to override and write line by line prints and basic tests just because I was raised on functional programming for recursion but returning `[root.val].append(left)` returns None but i assumed by BFS just wasn't finding the target
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # class TreeNode:
        #     def __init__(self, x):
        #         self.val = x
        #         self.left = None
        #         self.right = None
            
        #     def __str__(self):
        #         return str(self.val)
        # all vals are unique -> val ids the node
        # p != q and exists

        ###alg 1
        # find path to p,q
        # they both start at the root, then iterate left or right.
        # whenever the path for the two is different, the node before is the LCA because afterward they're on different subtrees

        def bfsPathFind(root: 'TreeNode', target: int) -> Optional[List['TreeNode']]:
            """final path should contain both root and target val, and should never be None unless None was the original input or there is not target node"""
            # print("====")
            # print(root)
            if root == None:
                # print("None")
                return None
            elif root.val == target:
                # print("reached target")
                return [root]
                
            # print("branch")
            left = bfsPathFind(root.left, target)
            # print(left)
            if left:
                # print("returning left")
                return [root] + left # NOOOOOOO: [root.val].append(left) #
            else:
                right = bfsPathFind(root.right, target)
                if right:
                    return [root] + right
                else:
                    return None
        
        # def bfsTest():
        #     l = TreeNode(1)
        #     root = TreeNode(0)
        #     root.left = l

        #     # assert bfsPathFind(root,0) == [0]
        #     print("TEST", bfsPathFind(root,1) == [0, 1])
        # bfsTest()
        

        path_to_p = bfsPathFind(root, p.val)
        path_to_q = bfsPathFind(root, q.val)
        # iterate and compare. Since target is p or q, and is included, the path will contain p or q. if p or q is parent of another, one whole list will be iterated through, and the other will still have branches to go down. so if the list is finished then it should be inclusive of that last target which is p or q
        i = 0
        while i < min(len(path_to_p), len(path_to_q)) and path_to_p[i] == path_to_q[i]:
            i+= 1
        return path_to_p[i-1]