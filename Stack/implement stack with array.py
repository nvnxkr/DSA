class Stack:
    def __init__(self):
        self.items = []

    def isempty(self):
        return len(self.items) == 0

    def push(self, val):
        self.items.append(val)

    def pop(self):
        if len(self.items) == 0:
            return "stack is empty"
        x = self.items.pop()
        print(f"{x} is popped")

    def top(self):
        if len(self.items) == 0:
            return "stack is empty"
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


st = Stack()
st.push(5)
st.push(10)
st.push(15)
st.push(25)
print(st)
st.size()
st.pop()
st.pop()
print(st.size())
print(st.top())
