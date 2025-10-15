# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
            
        return False
    
    def hasCycle(self, head):
        """two pointer -- fast, slow
        uses no memory / visited, just relies on the fact that either
        1. the list ends and returns False
        2. the list loops and 2n+1 laps and meets n
           **issue of like skipping each other repeatedly, like synced cycles that miss?"""
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
                
        return False

"""
Accepted
29 / 29 testcases passed
Morgann Thain
Morgann Thain
submitted at Oct 08, 2025 16:20

Editorial

Solution
Runtime
51
ms
Beats
38.93%
Analyze Complexity
Memory
20.01
MB
Beats
18.32%
"""