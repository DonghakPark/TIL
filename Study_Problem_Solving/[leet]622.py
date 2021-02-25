"""
Design Circular Queue Problem
Author : DongHak Park
Contact: donghark03@naver.com
"""

class MyCircularQueue:

    def __init__(self, k: int):
        self.Q = [-1] * k
        self.front = 0
        self.rear = -1
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.rear = (self.rear+1) % len(self.Q)
            self.Q[self.rear] = value
            self.count += 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            ret = self.Q[self.front]
            self.front = (self.front+1) % len(self.Q)
            self.count -= 1
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.Q[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.Q[self.rear]

    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.count == len(self.Q):
            return True
        else:
            return False


if __name__=="__main__":
    myCircularQueue = MyCircularQueue(3)
    print(myCircularQueue.enQueue(1))
    print(myCircularQueue.enQueue(2))
    print(myCircularQueue.enQueue(3))
    print(myCircularQueue.enQueue(4))

    print(myCircularQueue.Rear())
    print(myCircularQueue.isFull())
    print(myCircularQueue.deQueue())
    print(myCircularQueue.enQueue(4))
    print(myCircularQueue.Rear())
