class QueueUsingStack:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def dequeue(self):
        if len(self.s1) == 0:
            print("queue is empty")
            return -1
        self.s1.pop()

    def peek(self):
        if len(self.s1) == 0:
            print("queue is empty")
            return -1
        return self.s1[-1]


q = QueueUsingStack()
q.dequeue()
q.enqueue(2)
q.enqueue(5)
print(q.peek())
# q.dequeue()
print(q.s1)
