"""https://leetcode.com/problems/implement-queue-using-stacks/description/"""
class MyQueue:
    # Class variables are shared btw all instances and don't reset on creation and such
    # s1 = []
    # s2 = []
    # s1_has_elts = False
    # pop_is_fifo = False

    def __init__(self):
        # print("INIT")
        # print(f"s1,s2: {self.s1, self.s2}")
        self.s1 = []
        self.s2 = []
        self.s1_has_elts = False
        self.pop_is_fifo = False
        return
        
    def get_elts(self) -> tuple[list,list]:
        return (self.s1, self.s2) if self.s1_has_elts else (self.s2, self.s1)
    
    def flip_elts(self) -> None:
        print("FLIP START")
        elts, empty_list = self.get_elts()
        print(f"elts, empty_list: {elts, empty_list}")
        # if not pop_is_fifo:
        while elts:
            empty_list.append(elts.pop())


        self.s1_has_elts = not self.s1_has_elts
        self.pop_is_fifo = not self.pop_is_fifo
        print(f"elts, empty_list: {elts, empty_list}")


    def push(self, x: int) -> None:
        print(f"self.pop_is_fifo: {self.pop_is_fifo}")
        if self.pop_is_fifo:
            self.flip_elts()
        elts, empty_list = self.get_elts()
        elts.append(x)
        print(f"elts: {elts}")

    def pop(self) -> int:
        print("POP")
        print(f"self.pop_is_fifo: {self.pop_is_fifo}")
        if not self.pop_is_fifo:
            self.flip_elts()
        
        elts, empty_list = self.get_elts()
        return elts.pop()

    def peek(self) -> int:
        if not self.pop_is_fifo:
            self.flip_elts()
        elts, empty_list = self.get_elts()
        return elts[-1]
        

    def empty(self) -> bool:
        elts, empty_list = self.get_elts()
        print(elts, empty_list)
        return not bool(elts)
    
    
    """Accepted
22 / 22 testcases passed
Morgann Thain
Morgann Thain
submitted at Oct 15, 2025 16:20


Solution
Runtime
0
ms
Beats
100.00%
Analyze Complexity
Memory
18.07
MB
Beats
20.95%"""