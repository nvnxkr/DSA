class Queue:
    def __init__(self):
        self.items = []
        front = -1
        rear = -1

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        if len(self.items) == 0:
            return "Queue is empty"
        else:
            return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isempty(self):
        return len(self.items) == 0


q = Queue()
q.isempty()
q.enqueue(2)
q.enqueue(10)
print("size of Q is", q.size())
q.dequeue()
print(q.isempty())
print("size of Q is", q.size())
q.enqueue(5)
q.enqueue(10)
print(q.isempty())
print("size of Q is", q.size())
