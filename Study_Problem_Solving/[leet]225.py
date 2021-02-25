"""
Implement Stack using Queues
Author : DongHak Park
Contact: donghark03@naver.com
"""


class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        temp = []
        while len(self.stack) > 1:
            temp.append(self.stack.pop(0))
        ret = self.stack.pop(0)
        self.stack = temp
        return ret

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        else:
            return False
