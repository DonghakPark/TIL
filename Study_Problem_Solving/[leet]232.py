"""
Implement Queue Using Stacks Problem
Author : DongHak Park
Contact: donghark03@naver.com
"""

class MyQueue:
    def __init__(self):
        self.Q = []

    def push(self, x: int) -> None:
        self.Q.append(x)

    def pop(self) -> int:
        temp = []
        while len(self.Q) > 1:
            temp.append(self.Q.pop())
        ret = self.Q.pop()
        while temp:
            self.Q.append(temp.pop())
        return ret

    def peek(self) -> int:
        return self.Q[0]

    def empty(self) -> bool:
        if len(self.Q) == 0:
            return True
        else:
            return False
