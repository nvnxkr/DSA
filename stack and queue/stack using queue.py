from collections import deque


class StackUsingQueue:
    def __init__(self):
        self.queue = deque()

    def push(self, val):
        self.queue.append(val)

        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        if len(self.queue) == 0:
            return "queue is empty"
        return self.queue.popleft()

    def peek(self):
        return self.queue[0]


st = StackUsingQueue()
print(st.pop())
st.push(2)
st.push(5)
print(st.peek())
print(st.pop())
